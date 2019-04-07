#include <cstdlib>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
using namespace std;

class LZW {
public:
    LZW(string& list);
    ~LZW() {}
    void ChangeList(string& list);
    string GetList() { return strlist; }
    string Encode(string& source);
    string Decode(string& result);

private:
    string strlist;
    map<string, int> relation;
    string GetKey(int x);
    string ToHexStr(int x);
    int ToInt(string& hexstr);
};

LZW::LZW(string& list)
{
    for (int i = 0; i < list.size(); i++)
        relation.insert(make_pair(string(1, list[i]), i));
    relation.insert(make_pair(string("S_START"), list.size()));
    relation.insert(make_pair(string("S_END"), list.size() + 1));
    strlist = list;
}

void LZW::ChangeList(string& list)
{
    relation.clear();
    for (int i = 0; i < list.size(); i++)
        relation.insert(make_pair(string(1, list[i]), i));
    relation.insert(make_pair(string("S_START"), list.size()));
    relation.insert(make_pair(string("S_END"), list.size() + 1));
}

string LZW::Encode(string& source)
{
    int st = relation[string("S_START")], en = relation[string("S_END")];
    string result = to_string(st);
    string s1 = "", s2 = "";
    for (auto it = source.begin(); it != source.end(); it++) {
        s2 = *it;
        string tmp = s1 + s2;
        if (relation.find(tmp) != relation.end()) {
            s1 += s2;
            if (s1 == "")
                s1 = s2;
        } else {
            result += ToHexStr(relation[s1]);
            relation.insert(make_pair(tmp, relation.size()));
            s1 = s2;
        }
    }
    result += ToHexStr(relation[s1]);
    result += to_string(en);
    return result;
}

string LZW::GetKey(int x)
{
    for (auto it = relation.begin(); it != relation.end(); it++) {
        if (it->second == x)
            return it->first;
    }
    return "";
}

string LZW::ToHexStr(int x)
{
    string tmp;
    stringstream ss;
    ss << hex << x;
    ss >> tmp;
    ss.clear();
    ss.str("");
    return tmp;
}

int LZW::ToInt(string& hexstr)
{
    int tmp;
    stringstream ss;
    ss << hexstr;
    ss >> hex >> tmp;
    ss.clear();
    ss.str("");
    return tmp;
}

string LZW::Decode(string& result)
{
    string source;
    int st = relation[string("S_START")], en = relation[string("S_END")];
    string code = result.substr(0, 1), old = to_string(st);
    if (code != to_string(st))
        throw "Invalid String";
    for (int i = 1; i < result.size(); i++) {
        code = string(1, result[i]);
        if (GetKey(ToInt(code)) != "" && code != to_string(en)) {
            source += GetKey(ToInt(code));
            if (old != to_string(st)) {
                string tmp = GetKey(ToInt(old)) + GetKey(ToInt(code)).substr(0, 1);
                relation.insert(make_pair(tmp, relation.size()));
            }
            old = code;
        } else if (GetKey(ToInt(code)) == "") {
            string tmp = GetKey(ToInt(old)) + GetKey(ToInt(old)).substr(0, 1);
            source += tmp;
            relation.insert(make_pair(tmp, relation.size()));
            old = code;
        }
    }
    return source;
}

int main(void)
{
    system("title LZW编码器");
    cout << "Designed by LNP(LollipopNougat Popsicle)" << endl
         << "github https://github.com/lollipopnougat" << endl;
    cout << "重要提醒: 本程序仅测试了字符表为abcd 4个的情况!" << endl;
    string list;
    cout << "请输入字符表(字母): " << endl;
    cin >> list;
    try {
        LZW lzw(list);
        string input;
        int cmd;
        while (true) {
            cout << endl
                 << "选择功能" << endl
                 << "1: 修改字符表" << endl
                 << "2: LZW编码" << endl
                 << "3: LZW解码" << endl
                 << "4: 显示字符表" << endl
                 << "5: 清屏" << endl
                 << "0: 退出" << endl;
            cin >> cmd;
            switch (cmd) {
            case 1:
                cout << "输入新的字符表: " << endl;
                cin >> list;
                lzw.ChangeList(list);
                break;
            case 2:
                cout << "输入源字符串: " << endl;
                cin >> input;
                cout << "LZW编码结果" << lzw.Encode(input) << endl;
                break;
            case 3:
                cout << "输入待解字符串: " << endl;
                cin >> input;
                cout << "LZW解码结果" << lzw.Decode(input) << endl;
                break;
            case 4:
                cout << "字典: " << lzw.GetList() << endl;
                break;
            case 0:
                exit(0);
                break;
            case 5:
                system("cls");
                break;
            default:
                cout << "非法输入!" << endl;
            }
        }
    } catch (const char* st) {
        cerr << "Error! " << st << endl;
    }
    system("pause");
    return 0;
}