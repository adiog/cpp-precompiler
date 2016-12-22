import re

from src.PrettyPrintParserRuleContext import PrettyPrintParserRuleContext
# Generated from /home/adiog/workspace/cpp-precompiler/grammar/CPP14.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

from src.substitute import REPLACE


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0092")
        buf.write("\u0a04\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\3\2\5\2\u01a6\n\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u01b2\n\3\3\4\3\4\5\4")
        buf.write("\u01b6\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u01c1")
        buf.write("\n\5\3\6\3\6\5\6\u01c5\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u01d4\n\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u01db\n\7\3\7\3\7\3\7\7\7\u01e0\n\7\f\7\16\7")
        buf.write("\u01e3\13\7\3\b\3\b\5\b\u01e7\n\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("\u01ed\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u01f7\n")
        buf.write("\n\3\13\3\13\3\f\3\f\3\f\5\f\u01fe\n\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u0204\n\f\7\f\u0206\n\f\f\f\16\f\u0209\13\f\3\r\3")
        buf.write("\r\5\r\u020d\n\r\3\16\3\16\3\16\3\16\5\16\u0213\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u021a\n\17\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u0220\n\20\3\20\5\20\u0223\n\20\3\20\5\20\u0226")
        buf.write("\n\20\3\20\5\20\u0229\n\20\3\21\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u0230\n\21\3\21\3\21\3\21\3\21\3\21\5\21\u0237\n\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u026b\n\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u027a\n\21\3\21\3\21\3\21\3\21\5\21\u0280\n")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u0286\n\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0293\n")
        buf.write("\21\f\21\16\21\u0296\13\21\3\22\3\22\3\23\5\23\u029b\n")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u02aa\n\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u02b0\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u02ce")
        buf.write("\n\24\3\25\3\25\3\26\5\26\u02d3\n\26\3\26\3\26\5\26\u02d7")
        buf.write("\n\26\3\26\3\26\5\26\u02db\n\26\3\26\5\26\u02de\n\26\3")
        buf.write("\26\3\26\5\26\u02e2\n\26\3\26\3\26\3\26\3\26\5\26\u02e8")
        buf.write("\n\26\5\26\u02ea\n\26\3\27\3\27\3\27\3\27\3\30\3\30\5")
        buf.write("\30\u02f2\n\30\3\31\3\31\5\31\u02f6\n\31\3\31\5\31\u02f9")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u0300\n\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0307\n\32\7\32\u0309\n\32\f\32")
        buf.write("\16\32\u030c\13\32\3\33\3\33\5\33\u0310\n\33\3\33\3\33")
        buf.write("\5\33\u0314\n\33\3\34\5\34\u0317\n\34\3\34\3\34\3\34\5")
        buf.write("\34\u031c\n\34\3\34\3\34\3\34\3\34\5\34\u0322\n\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u032f\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\7\37\u033a\n\37\f\37\16\37\u033d\13\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \7 \u034b\n \f \16 \u034e\13")
        buf.write(" \3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u0359\n!\f!\16!\u035c")
        buf.write("\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0368")
        buf.write("\n\"\f\"\16\"\u036b\13\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\7#\u037c\n#\f#\16#\u037f\13#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\7$\u038a\n$\f$\16$\u038d\13$\3%\3")
        buf.write("%\3%\3%\3%\3%\7%\u0395\n%\f%\16%\u0398\13%\3&\3&\3&\3")
        buf.write("&\3&\3&\7&\u03a0\n&\f&\16&\u03a3\13&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\7\'\u03ab\n\'\f\'\16\'\u03ae\13\'\3(\3(\3(\3(\3")
        buf.write("(\3(\7(\u03b6\n(\f(\16(\u03b9\13(\3)\3)\3)\3)\3)\3)\7")
        buf.write(")\u03c1\n)\f)\16)\u03c4\13)\3*\3*\3*\3*\3*\3*\3*\5*\u03cd")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\5+\u03d5\n+\3,\3,\5,\u03d9\n,\3")
        buf.write("-\3-\3-\3-\5-\u03df\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\5.\u03ec\n.\3/\3/\3/\3/\3/\3/\7/\u03f4\n/\f/\16/\u03f7")
        buf.write("\13/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u03ff\n\60\f\60")
        buf.write("\16\60\u0402\13\60\3\61\3\61\3\62\3\62\5\62\u0408\n\62")
        buf.write("\3\62\3\62\5\62\u040c\n\62\3\62\3\62\5\62\u0410\n\62\3")
        buf.write("\62\3\62\5\62\u0414\n\62\3\62\3\62\5\62\u0418\n\62\3\62")
        buf.write("\3\62\3\62\5\62\u041d\n\62\3\62\5\62\u0420\n\62\3\63\3")
        buf.write("\63\3\63\5\63\u0425\n\63\3\64\5\64\u0428\n\64\3\64\3\64")
        buf.write("\3\64\3\64\5\64\u042e\n\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\5\64\u0436\n\64\3\64\3\64\3\64\5\64\u043b\n\64\3\65")
        buf.write("\5\65\u043e\n\65\3\65\3\65\3\66\5\66\u0443\n\66\3\66\3")
        buf.write("\66\3\67\3\67\5\67\u0449\n\67\3\67\3\67\38\38\58\u044f")
        buf.write("\n8\38\38\39\39\39\39\39\79\u0458\n9\f9\169\u045b\139")
        buf.write("\3:\3:\3:\3:\3:\7:\u0462\n:\f:\16:\u0465\13:\3;\3;\3;")
        buf.write("\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5")
        buf.write(";\u047b\n;\3<\3<\5<\u047f\n<\3<\3<\3<\3<\3<\3<\5<\u0487")
        buf.write("\n<\3<\3<\3<\3<\5<\u048d\n<\3=\3=\3=\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u04a1\n=\3=\3=\5=\u04a5")
        buf.write("\n=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\5=\u04b2\n=\3>\3")
        buf.write(">\5>\u04b6\n>\3?\5?\u04b9\n?\3?\3?\3?\3@\3@\5@\u04c0\n")
        buf.write("@\3A\3A\3A\3A\3A\3A\5A\u04c8\nA\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\5A\u04d2\nA\3B\3B\5B\u04d6\nB\3B\3B\3B\3B\3B\3B\5B\u04de")
        buf.write("\nB\3C\3C\3D\3D\3D\3D\3D\7D\u04e7\nD\fD\16D\u04ea\13D")
        buf.write("\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u04f6\nE\3F\3F\3F\3")
        buf.write("F\3F\3F\3F\3F\5F\u0500\nF\3G\3G\3G\5G\u0505\nG\3G\3G\3")
        buf.write("G\3G\3H\5H\u050c\nH\3H\5H\u050f\nH\3H\3H\3H\5H\u0514\n")
        buf.write("H\3H\3H\3H\5H\u0519\nH\3I\3I\3I\3I\3I\3I\3I\3I\3J\3J\3")
        buf.write("K\3K\3K\3L\3L\3L\3L\3L\3L\5L\u052e\nL\3M\3M\5M\u0532\n")
        buf.write("M\3M\3M\3M\5M\u0537\nM\3N\3N\3O\3O\3P\3P\3Q\3Q\3Q\5Q\u0542")
        buf.write("\nQ\3R\3R\3R\3R\5R\u0548\nR\3S\3S\5S\u054c\nS\3S\3S\3")
        buf.write("S\5S\u0551\nS\3T\3T\5T\u0555\nT\3T\3T\3T\5T\u055a\nT\3")
        buf.write("U\5U\u055d\nU\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\5U\u0573\nU\3V\3V\3V\3V\5V\u0579\n")
        buf.write("V\3W\3W\3W\3W\3W\3W\3W\3W\3W\5W\u0584\nW\3X\3X\5X\u0588")
        buf.write("\nX\3X\5X\u058b\nX\3X\3X\3X\3X\3X\3X\3X\3X\5X\u0595\n")
        buf.write("X\3X\3X\3X\3X\5X\u059b\nX\3X\5X\u059e\nX\3Y\3Y\3Z\3Z\3")
        buf.write("Z\5Z\u05a5\nZ\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\5Z\u05af\nZ\3[\3")
        buf.write("[\5[\u05b3\n[\3[\5[\u05b6\n[\3[\5[\u05b9\n[\3[\3[\5[\u05bd")
        buf.write("\n[\3[\3[\3[\5[\u05c2\n[\5[\u05c4\n[\3\\\3\\\5\\\u05c8")
        buf.write("\n\\\3\\\3\\\5\\\u05cc\n\\\3\\\3\\\3]\3]\3]\3]\3]\5]\u05d5")
        buf.write("\n]\3^\3^\3^\3_\3_\3_\3_\3_\3_\7_\u05e0\n_\f_\16_\u05e3")
        buf.write("\13_\3`\3`\3`\3`\3`\5`\u05ea\n`\3a\3a\3b\3b\5b\u05f0\n")
        buf.write("b\3c\3c\3d\3d\5d\u05f6\nd\3e\3e\5e\u05fa\ne\3f\5f\u05fd")
        buf.write("\nf\3f\3f\3f\3f\3f\3f\3g\5g\u0606\ng\3g\3g\3g\3g\3g\3")
        buf.write("g\3h\5h\u060f\nh\3h\3h\3h\3h\3h\3i\5i\u0617\ni\3j\3j\3")
        buf.write("k\3k\3k\3k\3k\3k\3l\5l\u0622\nl\3l\3l\3m\3m\5m\u0628\n")
        buf.write("m\3m\3m\3m\3m\3m\3m\3m\3m\3m\5m\u0633\nm\3n\5n\u0636\n")
        buf.write("n\3n\3n\3n\5n\u063b\nn\3n\3n\3n\3o\3o\3o\3o\3o\3o\3p\3")
        buf.write("p\3p\3p\5p\u064a\np\3p\3p\3p\3p\5p\u0650\np\3q\3q\3q\3")
        buf.write("q\3q\7q\u0657\nq\fq\16q\u065a\13q\3r\3r\3r\3r\3r\3r\3")
        buf.write("r\5r\u0663\nr\3s\3s\3s\3s\5s\u0669\ns\3s\3s\3s\3s\3s\3")
        buf.write("s\5s\u0671\ns\3s\3s\5s\u0675\ns\3t\3t\5t\u0679\nt\3t\3")
        buf.write("t\3t\5t\u067e\nt\3t\3t\3t\5t\u0683\nt\3t\3t\3t\3t\3t\7")
        buf.write("t\u068a\nt\ft\16t\u068d\13t\3u\3u\5u\u0691\nu\3v\3v\5")
        buf.write("v\u0695\nv\3w\3w\3w\3w\3x\3x\3y\3y\3y\3y\3z\3z\5z\u06a3")
        buf.write("\nz\3z\3z\7z\u06a7\nz\fz\16z\u06aa\13z\3{\3{\3{\3{\3{")
        buf.write("\3{\3{\3{\3{\3{\3{\3{\5{\u06b8\n{\3|\3|\3|\3|\3|\3|\7")
        buf.write("|\u06c0\n|\f|\16|\u06c3\13|\3}\3}\5}\u06c7\n}\3~\3~\3")
        buf.write("~\3~\3~\5~\u06ce\n~\3\177\3\177\3\177\3\177\5\177\u06d4")
        buf.write("\n\177\3\u0080\3\u0080\3\u0080\5\u0080\u06d9\n\u0080\3")
        buf.write("\u0080\3\u0080\3\u0080\3\u0080\5\u0080\u06df\n\u0080\3")
        buf.write("\u0080\3\u0080\3\u0080\3\u0080\3\u0080\5\u0080\u06e6\n")
        buf.write("\u0080\3\u0080\3\u0080\5\u0080\u06ea\n\u0080\7\u0080\u06ec")
        buf.write("\n\u0080\f\u0080\16\u0080\u06ef\13\u0080\3\u0081\3\u0081")
        buf.write("\3\u0081\3\u0081\5\u0081\u06f5\n\u0081\3\u0081\5\u0081")
        buf.write("\u06f8\n\u0081\3\u0081\5\u0081\u06fb\n\u0081\3\u0081\5")
        buf.write("\u0081\u06fe\n\u0081\3\u0082\3\u0082\3\u0082\5\u0082\u0703")
        buf.write("\n\u0082\3\u0083\3\u0083\5\u0083\u0707\n\u0083\3\u0083")
        buf.write("\5\u0083\u070a\n\u0083\3\u0083\3\u0083\5\u0083\u070e\n")
        buf.write("\u0083\3\u0083\3\u0083\5\u0083\u0712\n\u0083\3\u0083\3")
        buf.write("\u0083\3\u0083\5\u0083\u0717\n\u0083\3\u0083\5\u0083\u071a")
        buf.write("\n\u0083\5\u0083\u071c\n\u0083\3\u0084\3\u0084\5\u0084")
        buf.write("\u0720\n\u0084\3\u0085\3\u0085\3\u0086\3\u0086\3\u0087")
        buf.write("\5\u0087\u0727\n\u0087\3\u0087\3\u0087\3\u0088\3\u0088")
        buf.write("\5\u0088\u072d\n\u0088\3\u0089\3\u0089\5\u0089\u0731\n")
        buf.write("\u0089\3\u0089\3\u0089\3\u0089\3\u0089\5\u0089\u0737\n")
        buf.write("\u0089\3\u008a\3\u008a\3\u008a\5\u008a\u073c\n\u008a\5")
        buf.write("\u008a\u073e\n\u008a\3\u008b\3\u008b\3\u008b\3\u008b\5")
        buf.write("\u008b\u0744\n\u008b\3\u008b\3\u008b\5\u008b\u0748\n\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b\u074e\n\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\3\u008b\3\u008b\5\u008b\u0755")
        buf.write("\n\u008b\3\u008b\3\u008b\5\u008b\u0759\n\u008b\7\u008b")
        buf.write("\u075b\n\u008b\f\u008b\16\u008b\u075e\13\u008b\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008c\5\u008c\u0764\n\u008c\3\u008d")
        buf.write("\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write("\5\u008d\u076e\n\u008d\3\u008d\3\u008d\5\u008d\u0772\n")
        buf.write("\u008d\7\u008d\u0774\n\u008d\f\u008d\16\u008d\u0777\13")
        buf.write("\u008d\3\u008e\5\u008e\u077a\n\u008e\3\u008e\5\u008e\u077d")
        buf.write("\n\u008e\3\u008e\3\u008e\3\u008e\3\u008e\5\u008e\u0783")
        buf.write("\n\u008e\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\7\u008f\u078b\n\u008f\f\u008f\16\u008f\u078e\13\u008f")
        buf.write("\3\u0090\5\u0090\u0791\n\u0090\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\5\u0090\u0797\n\u0090\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\5\u0090\u079f\n\u0090\3\u0090")
        buf.write("\3\u0090\5\u0090\u07a3\n\u0090\3\u0090\5\u0090\u07a6\n")
        buf.write("\u0090\3\u0090\3\u0090\5\u0090\u07aa\n\u0090\3\u0090\3")
        buf.write("\u0090\3\u0090\5\u0090\u07af\n\u0090\3\u0091\5\u0091\u07b2")
        buf.write("\n\u0091\3\u0091\5\u0091\u07b5\n\u0091\3\u0091\3\u0091")
        buf.write("\5\u0091\u07b9\n\u0091\3\u0091\3\u0091\3\u0092\5\u0092")
        buf.write("\u07be\n\u0092\3\u0092\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write("\3\u0092\3\u0092\3\u0092\5\u0092\u07c8\n\u0092\3\u0093")
        buf.write("\5\u0093\u07cb\n\u0093\3\u0093\5\u0093\u07ce\n\u0093\3")
        buf.write("\u0093\3\u0093\5\u0093\u07d2\n\u0093\3\u0093\3\u0093\3")
        buf.write("\u0094\3\u0094\3\u0095\3\u0095\3\u0095\3\u0095\3\u0095")
        buf.write("\5\u0095\u07dd\n\u0095\3\u0096\3\u0096\3\u0096\5\u0096")
        buf.write("\u07e2\n\u0096\3\u0097\3\u0097\5\u0097\u07e6\n\u0097\3")
        buf.write("\u0098\3\u0098\3\u0098\5\u0098\u07eb\n\u0098\3\u0098\3")
        buf.write("\u0098\3\u0098\3\u0098\5\u0098\u07f1\n\u0098\7\u0098\u07f3")
        buf.write("\n\u0098\f\u0098\16\u0098\u07f6\13\u0098\3\u0099\3\u0099")
        buf.write("\3\u0099\5\u0099\u07fb\n\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\5\u0099\u0801\n\u0099\3\u009a\3\u009a\5\u009a")
        buf.write("\u0805\n\u009a\3\u009b\3\u009b\3\u009b\5\u009b\u080a\n")
        buf.write("\u009b\3\u009b\3\u009b\3\u009c\3\u009c\5\u009c\u0810\n")
        buf.write("\u009c\3\u009c\3\u009c\5\u009c\u0814\n\u009c\3\u009c\5")
        buf.write("\u009c\u0817\n\u009c\3\u009c\3\u009c\5\u009c\u081b\n\u009c")
        buf.write("\3\u009c\5\u009c\u081e\n\u009c\5\u009c\u0820\n\u009c\3")
        buf.write("\u009d\5\u009d\u0823\n\u009d\3\u009d\3\u009d\3\u009e\3")
        buf.write("\u009e\3\u009f\3\u009f\3\u00a0\3\u00a0\5\u00a0\u082d\n")
        buf.write("\u00a0\3\u00a0\3\u00a0\3\u00a0\5\u00a0\u0832\n\u00a0\5")
        buf.write("\u00a0\u0834\n\u00a0\3\u00a1\5\u00a1\u0837\n\u00a1\3\u00a1")
        buf.write("\5\u00a1\u083a\n\u00a1\3\u00a1\5\u00a1\u083d\n\u00a1\3")
        buf.write("\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write("\5\u00a1\u0846\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a2")
        buf.write("\3\u00a2\3\u00a2\7\u00a2\u084e\n\u00a2\f\u00a2\16\u00a2")
        buf.write("\u0851\13\u00a2\3\u00a3\3\u00a3\5\u00a3\u0855\n\u00a3")
        buf.write("\3\u00a3\5\u00a3\u0858\n\u00a3\3\u00a3\3\u00a3\5\u00a3")
        buf.write("\u085c\n\u00a3\3\u00a3\5\u00a3\u085f\n\u00a3\3\u00a3\5")
        buf.write("\u00a3\u0862\n\u00a3\3\u00a3\3\u00a3\5\u00a3\u0866\n\u00a3")
        buf.write("\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4\7\u00a4\u086d")
        buf.write("\n\u00a4\f\u00a4\16\u00a4\u0870\13\u00a4\3\u00a5\3\u00a5")
        buf.write("\3\u00a6\3\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\3\u00a8\3\u00a8\3\u00a8\5\u00a8\u087e\n\u00a8\3\u00a8")
        buf.write("\3\u00a8\3\u00a8\3\u00a8\5\u00a8\u0884\n\u00a8\7\u00a8")
        buf.write("\u0886\n\u00a8\f\u00a8\16\u00a8\u0889\13\u00a8\3\u00a9")
        buf.write("\5\u00a9\u088c\n\u00a9\3\u00a9\3\u00a9\5\u00a9\u0890\n")
        buf.write("\u00a9\3\u00a9\3\u00a9\5\u00a9\u0894\n\u00a9\3\u00a9\3")
        buf.write("\u00a9\5\u00a9\u0898\n\u00a9\3\u00a9\3\u00a9\5\u00a9\u089c")
        buf.write("\n\u00a9\3\u00a9\3\u00a9\5\u00a9\u08a0\n\u00a9\3\u00aa")
        buf.write("\5\u00aa\u08a3\n\u00aa\3\u00aa\3\u00aa\5\u00aa\u08a7\n")
        buf.write("\u00aa\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\3\u00ae\3\u00ae\5\u00ae\u08b2\n\u00ae\3\u00af")
        buf.write("\3\u00af\5\u00af\u08b6\n\u00af\3\u00b0\3\u00b0\3\u00b0")
        buf.write("\3\u00b1\3\u00b1\5\u00b1\u08bd\n\u00b1\3\u00b1\3\u00b1")
        buf.write("\5\u00b1\u08c1\n\u00b1\3\u00b1\3\u00b1\3\u00b1\5\u00b1")
        buf.write("\u08c6\n\u00b1\3\u00b2\3\u00b2\3\u00b2\5\u00b2\u08cb\n")
        buf.write("\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\3\u00b2\5\u00b2")
        buf.write("\u08d2\n\u00b2\3\u00b3\3\u00b3\5\u00b3\u08d6\n\u00b3\3")
        buf.write("\u00b4\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b5\3\u00b5")
        buf.write("\3\u00b5\5\u00b5\u08e0\n\u00b5\3\u00b6\3\u00b6\3\u00b6")
        buf.write("\3\u00b6\3\u00b6\3\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write("\3\u00b7\3\u00b7\7\u00b7\u08ee\n\u00b7\f\u00b7\16\u00b7")
        buf.write("\u08f1\13\u00b7\3\u00b8\3\u00b8\5\u00b8\u08f5\n\u00b8")
        buf.write("\3\u00b9\3\u00b9\5\u00b9\u08f9\n\u00b9\3\u00b9\5\u00b9")
        buf.write("\u08fc\n\u00b9\3\u00b9\3\u00b9\5\u00b9\u0900\n\u00b9\3")
        buf.write("\u00b9\3\u00b9\3\u00b9\3\u00b9\5\u00b9\u0906\n\u00b9\3")
        buf.write("\u00b9\5\u00b9\u0909\n\u00b9\3\u00b9\3\u00b9\5\u00b9\u090d")
        buf.write("\n\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\3\u00b9\3\u00b9\5\u00b9\u0917\n\u00b9\3\u00b9\5\u00b9")
        buf.write("\u091a\n\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\3\u00b9\5\u00b9\u0922\n\u00b9\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\5\u00b9\u0927\n\u00b9\3\u00ba\3\u00ba\3\u00ba\5\u00ba")
        buf.write("\u092c\n\u00ba\3\u00ba\3\u00ba\3\u00bb\3\u00bb\3\u00bb")
        buf.write("\3\u00bb\5\u00bb\u0934\n\u00bb\3\u00bb\3\u00bb\3\u00bb")
        buf.write("\3\u00bb\3\u00bb\5\u00bb\u093b\n\u00bb\3\u00bb\3\u00bb")
        buf.write("\5\u00bb\u093f\n\u00bb\3\u00bc\3\u00bc\3\u00bd\3\u00bd")
        buf.write("\3\u00bd\5\u00bd\u0946\n\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\3\u00bd\5\u00bd\u094c\n\u00bd\7\u00bd\u094e\n\u00bd\f")
        buf.write("\u00bd\16\u00bd\u0951\13\u00bd\3\u00be\3\u00be\3\u00be")
        buf.write("\5\u00be\u0956\n\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\3\u00bf\3\u00bf\5\u00bf\u095f\n\u00bf\3\u00bf")
        buf.write("\3\u00bf\5\u00bf\u0963\n\u00bf\3\u00c0\5\u00c0\u0966\n")
        buf.write("\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c1\3\u00c1\3\u00c1")
        buf.write("\3\u00c1\3\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c3")
        buf.write("\3\u00c3\5\u00c3\u0976\n\u00c3\3\u00c3\3\u00c3\3\u00c3")
        buf.write("\3\u00c4\3\u00c4\5\u00c4\u097d\n\u00c4\3\u00c5\3\u00c5")
        buf.write("\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c6\5\u00c6\u0986")
        buf.write("\n\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c6\5\u00c6\u098c")
        buf.write("\n\u00c6\3\u00c6\3\u00c6\5\u00c6\u0990\n\u00c6\3\u00c6")
        buf.write("\5\u00c6\u0993\n\u00c6\3\u00c7\3\u00c7\5\u00c7\u0997\n")
        buf.write("\u00c7\3\u00c8\3\u00c8\5\u00c8\u099b\n\u00c8\3\u00c9\3")
        buf.write("\u00c9\3\u00c9\5\u00c9\u09a0\n\u00c9\3\u00c9\3\u00c9\3")
        buf.write("\u00ca\3\u00ca\3\u00ca\5\u00ca\u09a7\n\u00ca\3\u00ca\3")
        buf.write("\u00ca\3\u00ca\3\u00ca\5\u00ca\u09ad\n\u00ca\7\u00ca\u09af")
        buf.write("\n\u00ca\f\u00ca\16\u00ca\u09b2\13\u00ca\3\u00cb\3\u00cb")
        buf.write("\3\u00cb\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u09ba\n\u00cb")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\5\u00ce")
        buf.write("\u09f3\n\u00ce\3\u00cf\3\u00cf\3\u00cf\3\u00cf\3\u00cf")
        buf.write("\3\u00cf\3\u00cf\5\u00cf\u09fc\n\u00cf\3\u00d0\3\u00d0")
        buf.write("\3\u00d1\3\u00d1\3\u00d2\3\u00d2\3\u00d2\2&\f\26 \62<")
        buf.write(">@BDFHJLNP\\^pr\u0086\u00bc\u00e0\u00e6\u00f2\u00f6\u00fe")
        buf.write("\u0114\u0118\u011c\u012e\u0142\u0146\u014e\u016c\u0178")
        buf.write("\u0192\u00d3\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2")
        buf.write("\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4")
        buf.write("\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6")
        buf.write("\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8")
        buf.write("\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea")
        buf.write("\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc")
        buf.write("\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e")
        buf.write("\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120")
        buf.write("\u0122\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132")
        buf.write("\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142\u0144")
        buf.write("\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156")
        buf.write("\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168")
        buf.write("\u016a\u016c\u016e\u0170\u0172\u0174\u0176\u0178\u017a")
        buf.write("\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a\u018c")
        buf.write("\u018e\u0190\u0192\u0194\u0196\u0198\u019a\u019c\u019e")
        buf.write("\u01a0\u01a2\2\r\4\2^^bb\4\2XZ^a\7\2!!,,\66\66<<CC\5\2")
        buf.write("\37\37))MM\4\2\21\21OO\4\2^^ss\5\2\20\20??JJ\4\2##\62")
        buf.write("\62\3\2\63\65\4\2\"\"EE\3\2\u008b\u008e\u0b2a\2\u01a5")
        buf.write("\3\2\2\2\4\u01b1\3\2\2\2\6\u01b5\3\2\2\2\b\u01c0\3\2\2")
        buf.write("\2\n\u01c2\3\2\2\2\f\u01d3\3\2\2\2\16\u01e4\3\2\2\2\20")
        buf.write("\u01ea\3\2\2\2\22\u01f6\3\2\2\2\24\u01f8\3\2\2\2\26\u01fa")
        buf.write("\3\2\2\2\30\u020c\3\2\2\2\32\u0212\3\2\2\2\34\u0219\3")
        buf.write("\2\2\2\36\u021b\3\2\2\2 \u026a\3\2\2\2\"\u0297\3\2\2\2")
        buf.write("$\u02af\3\2\2\2&\u02cd\3\2\2\2(\u02cf\3\2\2\2*\u02e9\3")
        buf.write("\2\2\2,\u02eb\3\2\2\2.\u02ef\3\2\2\2\60\u02f8\3\2\2\2")
        buf.write("\62\u02fa\3\2\2\2\64\u0313\3\2\2\2\66\u0321\3\2\2\28\u0323")
        buf.write("\3\2\2\2:\u032e\3\2\2\2<\u0330\3\2\2\2>\u033e\3\2\2\2")
        buf.write("@\u034f\3\2\2\2B\u035d\3\2\2\2D\u036c\3\2\2\2F\u0380\3")
        buf.write("\2\2\2H\u038e\3\2\2\2J\u0399\3\2\2\2L\u03a4\3\2\2\2N\u03af")
        buf.write("\3\2\2\2P\u03ba\3\2\2\2R\u03cc\3\2\2\2T\u03d4\3\2\2\2")
        buf.write("V\u03d8\3\2\2\2X\u03de\3\2\2\2Z\u03eb\3\2\2\2\\\u03ed")
        buf.write("\3\2\2\2^\u03f8\3\2\2\2`\u0403\3\2\2\2b\u041f\3\2\2\2")
        buf.write("d\u0424\3\2\2\2f\u043a\3\2\2\2h\u043d\3\2\2\2j\u0442\3")
        buf.write("\2\2\2l\u0446\3\2\2\2n\u044c\3\2\2\2p\u0452\3\2\2\2r\u045c")
        buf.write("\3\2\2\2t\u047a\3\2\2\2v\u048c\3\2\2\2x\u04b1\3\2\2\2")
        buf.write("z\u04b5\3\2\2\2|\u04b8\3\2\2\2~\u04bf\3\2\2\2\u0080\u04d1")
        buf.write("\3\2\2\2\u0082\u04dd\3\2\2\2\u0084\u04df\3\2\2\2\u0086")
        buf.write("\u04e1\3\2\2\2\u0088\u04f5\3\2\2\2\u008a\u04ff\3\2\2\2")
        buf.write("\u008c\u0501\3\2\2\2\u008e\u0518\3\2\2\2\u0090\u051a\3")
        buf.write("\2\2\2\u0092\u0522\3\2\2\2\u0094\u0524\3\2\2\2\u0096\u052d")
        buf.write("\3\2\2\2\u0098\u0536\3\2\2\2\u009a\u0538\3\2\2\2\u009c")
        buf.write("\u053a\3\2\2\2\u009e\u053c\3\2\2\2\u00a0\u0541\3\2\2\2")
        buf.write("\u00a2\u0547\3\2\2\2\u00a4\u0550\3\2\2\2\u00a6\u0559\3")
        buf.write("\2\2\2\u00a8\u0572\3\2\2\2\u00aa\u0578\3\2\2\2\u00ac\u0583")
        buf.write("\3\2\2\2\u00ae\u059d\3\2\2\2\u00b0\u059f\3\2\2\2\u00b2")
        buf.write("\u05ae\3\2\2\2\u00b4\u05c3\3\2\2\2\u00b6\u05c5\3\2\2\2")
        buf.write("\u00b8\u05d4\3\2\2\2\u00ba\u05d6\3\2\2\2\u00bc\u05d9\3")
        buf.write("\2\2\2\u00be\u05e9\3\2\2\2\u00c0\u05eb\3\2\2\2\u00c2\u05ef")
        buf.write("\3\2\2\2\u00c4\u05f1\3\2\2\2\u00c6\u05f5\3\2\2\2\u00c8")
        buf.write("\u05f9\3\2\2\2\u00ca\u05fc\3\2\2\2\u00cc\u0605\3\2\2\2")
        buf.write("\u00ce\u060e\3\2\2\2\u00d0\u0616\3\2\2\2\u00d2\u0618\3")
        buf.write("\2\2\2\u00d4\u061a\3\2\2\2\u00d6\u0621\3\2\2\2\u00d8\u0632")
        buf.write("\3\2\2\2\u00da\u0635\3\2\2\2\u00dc\u063f\3\2\2\2\u00de")
        buf.write("\u064f\3\2\2\2\u00e0\u0651\3\2\2\2\u00e2\u0662\3\2\2\2")
        buf.write("\u00e4\u0674\3\2\2\2\u00e6\u067d\3\2\2\2\u00e8\u068e\3")
        buf.write("\2\2\2\u00ea\u0694\3\2\2\2\u00ec\u0696\3\2\2\2\u00ee\u069a")
        buf.write("\3\2\2\2\u00f0\u069c\3\2\2\2\u00f2\u06a0\3\2\2\2\u00f4")
        buf.write("\u06b7\3\2\2\2\u00f6\u06b9\3\2\2\2\u00f8\u06c4\3\2\2\2")
        buf.write("\u00fa\u06cd\3\2\2\2\u00fc\u06d3\3\2\2\2\u00fe\u06de\3")
        buf.write("\2\2\2\u0100\u06f0\3\2\2\2\u0102\u06ff\3\2\2\2\u0104\u071b")
        buf.write("\3\2\2\2\u0106\u071d\3\2\2\2\u0108\u0721\3\2\2\2\u010a")
        buf.write("\u0723\3\2\2\2\u010c\u0726\3\2\2\2\u010e\u072a\3\2\2\2")
        buf.write("\u0110\u0736\3\2\2\2\u0112\u073d\3\2\2\2\u0114\u074d\3")
        buf.write("\2\2\2\u0116\u0763\3\2\2\2\u0118\u0765\3\2\2\2\u011a\u0782")
        buf.write("\3\2\2\2\u011c\u0784\3\2\2\2\u011e\u07ae\3\2\2\2\u0120")
        buf.write("\u07b1\3\2\2\2\u0122\u07c7\3\2\2\2\u0124\u07ca\3\2\2\2")
        buf.write("\u0126\u07d5\3\2\2\2\u0128\u07dc\3\2\2\2\u012a\u07e1\3")
        buf.write("\2\2\2\u012c\u07e5\3\2\2\2\u012e\u07e7\3\2\2\2\u0130\u0800")
        buf.write("\3\2\2\2\u0132\u0804\3\2\2\2\u0134\u0806\3\2\2\2\u0136")
        buf.write("\u081f\3\2\2\2\u0138\u0822\3\2\2\2\u013a\u0826\3\2\2\2")
        buf.write("\u013c\u0828\3\2\2\2\u013e\u0833\3\2\2\2\u0140\u0845\3")
        buf.write("\2\2\2\u0142\u0847\3\2\2\2\u0144\u0865\3\2\2\2\u0146\u0867")
        buf.write("\3\2\2\2\u0148\u0871\3\2\2\2\u014a\u0873\3\2\2\2\u014c")
        buf.write("\u0877\3\2\2\2\u014e\u087a\3\2\2\2\u0150\u089f\3\2\2\2")
        buf.write("\u0152\u08a6\3\2\2\2\u0154\u08a8\3\2\2\2\u0156\u08aa\3")
        buf.write("\2\2\2\u0158\u08ac\3\2\2\2\u015a\u08af\3\2\2\2\u015c\u08b3")
        buf.write("\3\2\2\2\u015e\u08b7\3\2\2\2\u0160\u08c5\3\2\2\2\u0162")
        buf.write("\u08d1\3\2\2\2\u0164\u08d5\3\2\2\2\u0166\u08d7\3\2\2\2")
        buf.write("\u0168\u08df\3\2\2\2\u016a\u08e1\3\2\2\2\u016c\u08e7\3")
        buf.write("\2\2\2\u016e\u08f4\3\2\2\2\u0170\u0926\3\2\2\2\u0172\u0928")
        buf.write("\3\2\2\2\u0174\u093e\3\2\2\2\u0176\u0940\3\2\2\2\u0178")
        buf.write("\u0942\3\2\2\2\u017a\u0955\3\2\2\2\u017c\u0962\3\2\2\2")
        buf.write("\u017e\u0965\3\2\2\2\u0180\u096a\3\2\2\2\u0182\u096f\3")
        buf.write("\2\2\2\u0184\u0973\3\2\2\2\u0186\u097a\3\2\2\2\u0188\u097e")
        buf.write("\3\2\2\2\u018a\u0992\3\2\2\2\u018c\u0994\3\2\2\2\u018e")
        buf.write("\u099a\3\2\2\2\u0190\u099c\3\2\2\2\u0192\u09a3\3\2\2\2")
        buf.write("\u0194\u09b9\3\2\2\2\u0196\u09bb\3\2\2\2\u0198\u09be\3")
        buf.write("\2\2\2\u019a\u09f2\3\2\2\2\u019c\u09fb\3\2\2\2\u019e\u09fd")
        buf.write("\3\2\2\2\u01a0\u09ff\3\2\2\2\u01a2\u0a01\3\2\2\2\u01a4")
        buf.write("\u01a6\5\u0086D\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2")
        buf.write("\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\7\2\2\3\u01a8\3\3")
        buf.write("\2\2\2\u01a9\u01b2\5\u019c\u00cf\2\u01aa\u01b2\7B\2\2")
        buf.write("\u01ab\u01ac\7R\2\2\u01ac\u01ad\5\\/\2\u01ad\u01ae\7S")
        buf.write("\2\2\u01ae\u01b2\3\2\2\2\u01af\u01b2\5\6\4\2\u01b0\u01b2")
        buf.write("\5\16\b\2\u01b1\u01a9\3\2\2\2\u01b1\u01aa\3\2\2\2\u01b1")
        buf.write("\u01ab\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2")
        buf.write("\u01b2\5\3\2\2\2\u01b3\u01b6\5\b\5\2\u01b4\u01b6\5\n\6")
        buf.write("\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\7\3\2")
        buf.write("\2\2\u01b7\u01c1\7\u0081\2\2\u01b8\u01c1\5\u0166\u00b4")
        buf.write("\2\u01b9\u01c1\5\u0158\u00ad\2\u01ba\u01c1\5\u0168\u00b5")
        buf.write("\2\u01bb\u01bc\7`\2\2\u01bc\u01c1\5\u0132\u009a\2\u01bd")
        buf.write("\u01be\7`\2\2\u01be\u01c1\5\u00acW\2\u01bf\u01c1\5\u0174")
        buf.write("\u00bb\2\u01c0\u01b7\3\2\2\2\u01c0\u01b8\3\2\2\2\u01c0")
        buf.write("\u01b9\3\2\2\2\u01c0\u01ba\3\2\2\2\u01c0\u01bb\3\2\2\2")
        buf.write("\u01c0\u01bd\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1\t\3\2\2")
        buf.write("\2\u01c2\u01c4\5\f\7\2\u01c3\u01c5\7A\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c7\5\b\5\2\u01c7\13\3\2\2\2\u01c8\u01c9\b\7\1\2\u01c9")
        buf.write("\u01d4\7|\2\2\u01ca\u01cb\5\u00aaV\2\u01cb\u01cc\7|\2")
        buf.write("\2\u01cc\u01d4\3\2\2\2\u01cd\u01ce\5\u00c2b\2\u01ce\u01cf")
        buf.write("\7|\2\2\u01cf\u01d4\3\2\2\2\u01d0\u01d1\5\u00acW\2\u01d1")
        buf.write("\u01d2\7|\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01c8\3\2\2\2")
        buf.write("\u01d3\u01ca\3\2\2\2\u01d3\u01cd\3\2\2\2\u01d3\u01d0\3")
        buf.write("\2\2\2\u01d4\u01e1\3\2\2\2\u01d5\u01d6\f\4\2\2\u01d6\u01d7")
        buf.write("\7\u0081\2\2\u01d7\u01e0\7|\2\2\u01d8\u01da\f\3\2\2\u01d9")
        buf.write("\u01db\7A\2\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01dd\5\u0172\u00ba\2\u01dd")
        buf.write("\u01de\7|\2\2\u01de\u01e0\3\2\2\2\u01df\u01d5\3\2\2\2")
        buf.write("\u01df\u01d8\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\r\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e4\u01e6\5\20\t\2\u01e5\u01e7\5\36\20\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e9\5l\67\2\u01e9\17\3\2\2\2\u01ea\u01ec\7T\2")
        buf.write("\2\u01eb\u01ed\5\22\n\2\u01ec\u01eb\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\7U\2\2\u01ef")
        buf.write("\21\3\2\2\2\u01f0\u01f7\5\24\13\2\u01f1\u01f7\5\26\f\2")
        buf.write("\u01f2\u01f3\5\24\13\2\u01f3\u01f4\7w\2\2\u01f4\u01f5")
        buf.write("\5\26\f\2\u01f5\u01f7\3\2\2\2\u01f6\u01f0\3\2\2\2\u01f6")
        buf.write("\u01f1\3\2\2\2\u01f6\u01f2\3\2\2\2\u01f7\23\3\2\2\2\u01f8")
        buf.write("\u01f9\t\2\2\2\u01f9\25\3\2\2\2\u01fa\u01fb\b\f\1\2\u01fb")
        buf.write("\u01fd\5\30\r\2\u01fc\u01fe\7\u0080\2\2\u01fd\u01fc\3")
        buf.write("\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0207\3\2\2\2\u01ff\u0200")
        buf.write("\f\3\2\2\u0200\u0201\7w\2\2\u0201\u0203\5\30\r\2\u0202")
        buf.write("\u0204\7\u0080\2\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2")
        buf.write("\2\2\u0204\u0206\3\2\2\2\u0205\u01ff\3\2\2\2\u0206\u0209")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\27\3\2\2\2\u0209\u0207\3\2\2\2\u020a\u020d\5\32\16\2")
        buf.write("\u020b\u020d\5\34\17\2\u020c\u020a\3\2\2\2\u020c\u020b")
        buf.write("\3\2\2\2\u020d\31\3\2\2\2\u020e\u0213\7\u0081\2\2\u020f")
        buf.write("\u0210\7^\2\2\u0210\u0213\7\u0081\2\2\u0211\u0213\7B\2")
        buf.write("\2\u0212\u020e\3\2\2\2\u0212\u020f\3\2\2\2\u0212\u0211")
        buf.write("\3\2\2\2\u0213\33\3\2\2\2\u0214\u0215\7\u0081\2\2\u0215")
        buf.write("\u021a\5\u0128\u0095\2\u0216\u0217\7^\2\2\u0217\u0218")
        buf.write("\7\u0081\2\2\u0218\u021a\5\u0128\u0095\2\u0219\u0214\3")
        buf.write("\2\2\2\u0219\u0216\3\2\2\2\u021a\35\3\2\2\2\u021b\u021c")
        buf.write("\7R\2\2\u021c\u021d\5\u011a\u008e\2\u021d\u021f\7S\2\2")
        buf.write("\u021e\u0220\7,\2\2\u021f\u021e\3\2\2\2\u021f\u0220\3")
        buf.write("\2\2\2\u0220\u0222\3\2\2\2\u0221\u0223\5\u018e\u00c8\2")
        buf.write("\u0222\u0221\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3")
        buf.write("\2\2\2\u0224\u0226\5\u00e0q\2\u0225\u0224\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0226\u0228\3\2\2\2\u0227\u0229\5\u0102")
        buf.write("\u0082\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\37\3\2\2\2\u022a\u022b\b\21\1\2\u022b\u026b\5\4\3\2\u022c")
        buf.write("\u022d\5\u00a8U\2\u022d\u022f\7R\2\2\u022e\u0230\5\"\22")
        buf.write("\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0232\7S\2\2\u0232\u026b\3\2\2\2\u0233")
        buf.write("\u0234\5\u017c\u00bf\2\u0234\u0236\7R\2\2\u0235\u0237")
        buf.write("\5\"\22\2\u0236\u0235\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u0239\7S\2\2\u0239\u026b\3\2\2\2")
        buf.write("\u023a\u023b\5\u00a8U\2\u023b\u023c\5\u0130\u0099\2\u023c")
        buf.write("\u026b\3\2\2\2\u023d\u023e\5\u017c\u00bf\2\u023e\u023f")
        buf.write("\5\u0130\u0099\2\u023f\u026b\3\2\2\2\u0240\u0241\7\34")
        buf.write("\2\2\u0241\u0242\7c\2\2\u0242\u0243\5\u010e\u0088\2\u0243")
        buf.write("\u0244\7d\2\2\u0244\u0245\7R\2\2\u0245\u0246\5\\/\2\u0246")
        buf.write("\u0247\7S\2\2\u0247\u026b\3\2\2\2\u0248\u0249\7>\2\2\u0249")
        buf.write("\u024a\7c\2\2\u024a\u024b\5\u010e\u0088\2\u024b\u024c")
        buf.write("\7d\2\2\u024c\u024d\7R\2\2\u024d\u024e\5\\/\2\u024e\u024f")
        buf.write("\7S\2\2\u024f\u026b\3\2\2\2\u0250\u0251\7\67\2\2\u0251")
        buf.write("\u0252\7c\2\2\u0252\u0253\5\u010e\u0088\2\u0253\u0254")
        buf.write("\7d\2\2\u0254\u0255\7R\2\2\u0255\u0256\5\\/\2\u0256\u0257")
        buf.write("\7S\2\2\u0257\u026b\3\2\2\2\u0258\u0259\7\23\2\2\u0259")
        buf.write("\u025a\7c\2\2\u025a\u025b\5\u010e\u0088\2\u025b\u025c")
        buf.write("\7d\2\2\u025c\u025d\7R\2\2\u025d\u025e\5\\/\2\u025e\u025f")
        buf.write("\7S\2\2\u025f\u026b\3\2\2\2\u0260\u0261\7H\2\2\u0261\u0262")
        buf.write("\7R\2\2\u0262\u0263\5\\/\2\u0263\u0264\7S\2\2\u0264\u026b")
        buf.write("\3\2\2\2\u0265\u0266\7H\2\2\u0266\u0267\7R\2\2\u0267\u0268")
        buf.write("\5\u010e\u0088\2\u0268\u0269\7S\2\2\u0269\u026b\3\2\2")
        buf.write("\2\u026a\u022a\3\2\2\2\u026a\u022c\3\2\2\2\u026a\u0233")
        buf.write("\3\2\2\2\u026a\u023a\3\2\2\2\u026a\u023d\3\2\2\2\u026a")
        buf.write("\u0240\3\2\2\2\u026a\u0248\3\2\2\2\u026a\u0250\3\2\2\2")
        buf.write("\u026a\u0258\3\2\2\2\u026a\u0260\3\2\2\2\u026a\u0265\3")
        buf.write("\2\2\2\u026b\u0294\3\2\2\2\u026c\u026d\f\25\2\2\u026d")
        buf.write("\u026e\7T\2\2\u026e\u026f\5\\/\2\u026f\u0270\7U\2\2\u0270")
        buf.write("\u0293\3\2\2\2\u0271\u0272\f\24\2\2\u0272\u0273\7T\2\2")
        buf.write("\u0273\u0274\5\u0130\u0099\2\u0274\u0275\7U\2\2\u0275")
        buf.write("\u0293\3\2\2\2\u0276\u0277\f\23\2\2\u0277\u0279\7R\2\2")
        buf.write("\u0278\u027a\5\"\22\2\u0279\u0278\3\2\2\2\u0279\u027a")
        buf.write("\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u0293\7S\2\2\u027c")
        buf.write("\u027d\f\16\2\2\u027d\u027f\7~\2\2\u027e\u0280\7A\2\2")
        buf.write("\u027f\u027e\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281\3")
        buf.write("\2\2\2\u0281\u0293\5\6\4\2\u0282\u0283\f\r\2\2\u0283\u0285")
        buf.write("\7y\2\2\u0284\u0286\7A\2\2\u0285\u0284\3\2\2\2\u0285\u0286")
        buf.write("\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0293\5\6\4\2\u0288")
        buf.write("\u0289\f\f\2\2\u0289\u028a\7~\2\2\u028a\u0293\5$\23\2")
        buf.write("\u028b\u028c\f\13\2\2\u028c\u028d\7y\2\2\u028d\u0293\5")
        buf.write("$\23\2\u028e\u028f\f\n\2\2\u028f\u0293\7u\2\2\u0290\u0291")
        buf.write("\f\t\2\2\u0291\u0293\7v\2\2\u0292\u026c\3\2\2\2\u0292")
        buf.write("\u0271\3\2\2\2\u0292\u0276\3\2\2\2\u0292\u027c\3\2\2\2")
        buf.write("\u0292\u0282\3\2\2\2\u0292\u0288\3\2\2\2\u0292\u028b\3")
        buf.write("\2\2\2\u0292\u028e\3\2\2\2\u0292\u0290\3\2\2\2\u0293\u0296")
        buf.write("\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2\2\2\u0295")
        buf.write("!\3\2\2\2\u0296\u0294\3\2\2\2\u0297\u0298\5\u012e\u0098")
        buf.write("\2\u0298#\3\2\2\2\u0299\u029b\5\f\7\2\u029a\u0299\3\2")
        buf.write("\2\2\u029a\u029b\3\2\2\2\u029b\u029c\3\2\2\2\u029c\u029d")
        buf.write("\5\u00aaV\2\u029d\u029e\7|\2\2\u029e\u029f\7`\2\2\u029f")
        buf.write("\u02a0\5\u00aaV\2\u02a0\u02b0\3\2\2\2\u02a1\u02a2\5\f")
        buf.write("\7\2\u02a2\u02a3\7A\2\2\u02a3\u02a4\5\u0172\u00ba\2\u02a4")
        buf.write("\u02a5\7|\2\2\u02a5\u02a6\7`\2\2\u02a6\u02a7\5\u00aaV")
        buf.write("\2\u02a7\u02b0\3\2\2\2\u02a8\u02aa\5\f\7\2\u02a9\u02a8")
        buf.write("\3\2\2\2\u02a9\u02aa\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab")
        buf.write("\u02ac\7`\2\2\u02ac\u02b0\5\u00aaV\2\u02ad\u02ae\7`\2")
        buf.write("\2\u02ae\u02b0\5\u00acW\2\u02af\u029a\3\2\2\2\u02af\u02a1")
        buf.write("\3\2\2\2\u02af\u02a9\3\2\2\2\u02af\u02ad\3\2\2\2\u02b0")
        buf.write("%\3\2\2\2\u02b1\u02ce\5 \21\2\u02b2\u02b3\7u\2\2\u02b3")
        buf.write("\u02ce\5:\36\2\u02b4\u02b5\7v\2\2\u02b5\u02ce\5:\36\2")
        buf.write("\u02b6\u02b7\5(\25\2\u02b7\u02b8\5:\36\2\u02b8\u02ce\3")
        buf.write("\2\2\2\u02b9\u02ba\7;\2\2\u02ba\u02ce\5&\24\2\u02bb\u02bc")
        buf.write("\7;\2\2\u02bc\u02bd\7R\2\2\u02bd\u02be\5\u010e\u0088\2")
        buf.write("\u02be\u02bf\7S\2\2\u02bf\u02ce\3\2\2\2\u02c0\u02c1\7")
        buf.write(";\2\2\u02c1\u02c2\7\u0080\2\2\u02c2\u02c3\7R\2\2\u02c3")
        buf.write("\u02c4\7\u0081\2\2\u02c4\u02ce\7S\2\2\u02c5\u02c6\7\6")
        buf.write("\2\2\u02c6\u02c7\7R\2\2\u02c7\u02c8\5\u010e\u0088\2\u02c8")
        buf.write("\u02c9\7S\2\2\u02c9\u02ce\3\2\2\2\u02ca\u02ce\58\35\2")
        buf.write("\u02cb\u02ce\5*\26\2\u02cc\u02ce\5\66\34\2\u02cd\u02b1")
        buf.write("\3\2\2\2\u02cd\u02b2\3\2\2\2\u02cd\u02b4\3\2\2\2\u02cd")
        buf.write("\u02b6\3\2\2\2\u02cd\u02b9\3\2\2\2\u02cd\u02bb\3\2\2\2")
        buf.write("\u02cd\u02c0\3\2\2\2\u02cd\u02c5\3\2\2\2\u02cd\u02ca\3")
        buf.write("\2\2\2\u02cd\u02cb\3\2\2\2\u02cd\u02cc\3\2\2\2\u02ce\'")
        buf.write("\3\2\2\2\u02cf\u02d0\t\3\2\2\u02d0)\3\2\2\2\u02d1\u02d3")
        buf.write("\7|\2\2\u02d2\u02d1\3\2\2\2\u02d2\u02d3\3\2\2\2\u02d3")
        buf.write("\u02d4\3\2\2\2\u02d4\u02d6\7.\2\2\u02d5\u02d7\5,\27\2")
        buf.write("\u02d6\u02d5\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u02d8\3")
        buf.write("\2\2\2\u02d8\u02da\5.\30\2\u02d9\u02db\5\64\33\2\u02da")
        buf.write("\u02d9\3\2\2\2\u02da\u02db\3\2\2\2\u02db\u02ea\3\2\2\2")
        buf.write("\u02dc\u02de\7|\2\2\u02dd\u02dc\3\2\2\2\u02dd\u02de\3")
        buf.write("\2\2\2\u02de\u02df\3\2\2\2\u02df\u02e1\7.\2\2\u02e0\u02e2")
        buf.write("\5,\27\2\u02e1\u02e0\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2")
        buf.write("\u02e3\3\2\2\2\u02e3\u02e4\7R\2\2\u02e4\u02e5\5\u010e")
        buf.write("\u0088\2\u02e5\u02e7\7S\2\2\u02e6\u02e8\5\64\33\2\u02e7")
        buf.write("\u02e6\3\2\2\2\u02e7\u02e8\3\2\2\2\u02e8\u02ea\3\2\2\2")
        buf.write("\u02e9\u02d2\3\2\2\2\u02e9\u02dd\3\2\2\2\u02ea+\3\2\2")
        buf.write("\2\u02eb\u02ec\7R\2\2\u02ec\u02ed\5\"\22\2\u02ed\u02ee")
        buf.write("\7S\2\2\u02ee-\3\2\2\2\u02ef\u02f1\5\u00a4S\2\u02f0\u02f2")
        buf.write("\5\60\31\2\u02f1\u02f0\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2")
        buf.write("/\3\2\2\2\u02f3\u02f5\5\u0104\u0083\2\u02f4\u02f6\5\60")
        buf.write("\31\2\u02f5\u02f4\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02f9")
        buf.write("\3\2\2\2\u02f7\u02f9\5\62\32\2\u02f8\u02f3\3\2\2\2\u02f8")
        buf.write("\u02f7\3\2\2\2\u02f9\61\3\2\2\2\u02fa\u02fb\b\32\1\2\u02fb")
        buf.write("\u02fc\7T\2\2\u02fc\u02fd\5\\/\2\u02fd\u02ff\7U\2\2\u02fe")
        buf.write("\u0300\5\u00e0q\2\u02ff\u02fe\3\2\2\2\u02ff\u0300\3\2")
        buf.write("\2\2\u0300\u030a\3\2\2\2\u0301\u0302\f\3\2\2\u0302\u0303")
        buf.write("\7T\2\2\u0303\u0304\5`\61\2\u0304\u0306\7U\2\2\u0305\u0307")
        buf.write("\5\u00e0q\2\u0306\u0305\3\2\2\2\u0306\u0307\3\2\2\2\u0307")
        buf.write("\u0309\3\2\2\2\u0308\u0301\3\2\2\2\u0309\u030c\3\2\2\2")
        buf.write("\u030a\u0308\3\2\2\2\u030a\u030b\3\2\2\2\u030b\63\3\2")
        buf.write("\2\2\u030c\u030a\3\2\2\2\u030d\u030f\7R\2\2\u030e\u0310")
        buf.write("\5\"\22\2\u030f\u030e\3\2\2\2\u030f\u0310\3\2\2\2\u0310")
        buf.write("\u0311\3\2\2\2\u0311\u0314\7S\2\2\u0312\u0314\5\u0130")
        buf.write("\u0099\2\u0313\u030d\3\2\2\2\u0313\u0312\3\2\2\2\u0314")
        buf.write("\65\3\2\2\2\u0315\u0317\7|\2\2\u0316\u0315\3\2\2\2\u0316")
        buf.write("\u0317\3\2\2\2\u0317\u0318\3\2\2\2\u0318\u0319\7\31\2")
        buf.write("\2\u0319\u0322\5:\36\2\u031a\u031c\7|\2\2\u031b\u031a")
        buf.write("\3\2\2\2\u031b\u031c\3\2\2\2\u031c\u031d\3\2\2\2\u031d")
        buf.write("\u031e\7\31\2\2\u031e\u031f\7T\2\2\u031f\u0320\7U\2\2")
        buf.write("\u0320\u0322\5:\36\2\u0321\u0316\3\2\2\2\u0321\u031b\3")
        buf.write("\2\2\2\u0322\67\3\2\2\2\u0323\u0324\7/\2\2\u0324\u0325")
        buf.write("\7R\2\2\u0325\u0326\5\\/\2\u0326\u0327\7S\2\2\u03279\3")
        buf.write("\2\2\2\u0328\u032f\5&\24\2\u0329\u032a\7R\2\2\u032a\u032b")
        buf.write("\5\u010e\u0088\2\u032b\u032c\7S\2\2\u032c\u032d\5:\36")
        buf.write("\2\u032d\u032f\3\2\2\2\u032e\u0328\3\2\2\2\u032e\u0329")
        buf.write("\3\2\2\2\u032f;\3\2\2\2\u0330\u0331\b\37\1\2\u0331\u0332")
        buf.write("\5:\36\2\u0332\u033b\3\2\2\2\u0333\u0334\f\4\2\2\u0334")
        buf.write("\u0335\7\177\2\2\u0335\u033a\5:\36\2\u0336\u0337\f\3\2")
        buf.write("\2\u0337\u0338\7x\2\2\u0338\u033a\5:\36\2\u0339\u0333")
        buf.write("\3\2\2\2\u0339\u0336\3\2\2\2\u033a\u033d\3\2\2\2\u033b")
        buf.write("\u0339\3\2\2\2\u033b\u033c\3\2\2\2\u033c=\3\2\2\2\u033d")
        buf.write("\u033b\3\2\2\2\u033e\u033f\b \1\2\u033f\u0340\5<\37\2")
        buf.write("\u0340\u034c\3\2\2\2\u0341\u0342\f\5\2\2\u0342\u0343\7")
        buf.write("Z\2\2\u0343\u034b\5<\37\2\u0344\u0345\f\4\2\2\u0345\u0346")
        buf.write("\7[\2\2\u0346\u034b\5<\37\2\u0347\u0348\f\3\2\2\u0348")
        buf.write("\u0349\7\\\2\2\u0349\u034b\5<\37\2\u034a\u0341\3\2\2\2")
        buf.write("\u034a\u0344\3\2\2\2\u034a\u0347\3\2\2\2\u034b\u034e\3")
        buf.write("\2\2\2\u034c\u034a\3\2\2\2\u034c\u034d\3\2\2\2\u034d?")
        buf.write("\3\2\2\2\u034e\u034c\3\2\2\2\u034f\u0350\b!\1\2\u0350")
        buf.write("\u0351\5> \2\u0351\u035a\3\2\2\2\u0352\u0353\f\4\2\2\u0353")
        buf.write("\u0354\7X\2\2\u0354\u0359\5> \2\u0355\u0356\f\3\2\2\u0356")
        buf.write("\u0357\7Y\2\2\u0357\u0359\5> \2\u0358\u0352\3\2\2\2\u0358")
        buf.write("\u0355\3\2\2\2\u0359\u035c\3\2\2\2\u035a\u0358\3\2\2\2")
        buf.write("\u035a\u035b\3\2\2\2\u035bA\3\2\2\2\u035c\u035a\3\2\2")
        buf.write("\2\u035d\u035e\b\"\1\2\u035e\u035f\5@!\2\u035f\u0369\3")
        buf.write("\2\2\2\u0360\u0361\f\4\2\2\u0361\u0362\7m\2\2\u0362\u0368")
        buf.write("\5@!\2\u0363\u0364\f\3\2\2\u0364\u0365\5\u0196\u00cc\2")
        buf.write("\u0365\u0366\5@!\2\u0366\u0368\3\2\2\2\u0367\u0360\3\2")
        buf.write("\2\2\u0367\u0363\3\2\2\2\u0368\u036b\3\2\2\2\u0369\u0367")
        buf.write("\3\2\2\2\u0369\u036a\3\2\2\2\u036aC\3\2\2\2\u036b\u0369")
        buf.write("\3\2\2\2\u036c\u036d\b#\1\2\u036d\u036e\5B\"\2\u036e\u037d")
        buf.write("\3\2\2\2\u036f\u0370\f\6\2\2\u0370\u0371\7c\2\2\u0371")
        buf.write("\u037c\5B\"\2\u0372\u0373\f\5\2\2\u0373\u0374\7d\2\2\u0374")
        buf.write("\u037c\5B\"\2\u0375\u0376\f\4\2\2\u0376\u0377\7q\2\2\u0377")
        buf.write("\u037c\5B\"\2\u0378\u0379\f\3\2\2\u0379\u037a\7r\2\2\u037a")
        buf.write("\u037c\5B\"\2\u037b\u036f\3\2\2\2\u037b\u0372\3\2\2\2")
        buf.write("\u037b\u0375\3\2\2\2\u037b\u0378\3\2\2\2\u037c\u037f\3")
        buf.write("\2\2\2\u037d\u037b\3\2\2\2\u037d\u037e\3\2\2\2\u037eE")
        buf.write("\3\2\2\2\u037f\u037d\3\2\2\2\u0380\u0381\b$\1\2\u0381")
        buf.write("\u0382\5D#\2\u0382\u038b\3\2\2\2\u0383\u0384\f\4\2\2\u0384")
        buf.write("\u0385\7o\2\2\u0385\u038a\5D#\2\u0386\u0387\f\3\2\2\u0387")
        buf.write("\u0388\7p\2\2\u0388\u038a\5D#\2\u0389\u0383\3\2\2\2\u0389")
        buf.write("\u0386\3\2\2\2\u038a\u038d\3\2\2\2\u038b\u0389\3\2\2\2")
        buf.write("\u038b\u038c\3\2\2\2\u038cG\3\2\2\2\u038d\u038b\3\2\2")
        buf.write("\2\u038e\u038f\b%\1\2\u038f\u0390\5F$\2\u0390\u0396\3")
        buf.write("\2\2\2\u0391\u0392\f\3\2\2\u0392\u0393\7^\2\2\u0393\u0395")
        buf.write("\5F$\2\u0394\u0391\3\2\2\2\u0395\u0398\3\2\2\2\u0396\u0394")
        buf.write("\3\2\2\2\u0396\u0397\3\2\2\2\u0397I\3\2\2\2\u0398\u0396")
        buf.write("\3\2\2\2\u0399\u039a\b&\1\2\u039a\u039b\5H%\2\u039b\u03a1")
        buf.write("\3\2\2\2\u039c\u039d\f\3\2\2\u039d\u039e\7]\2\2\u039e")
        buf.write("\u03a0\5H%\2\u039f\u039c\3\2\2\2\u03a0\u03a3\3\2\2\2\u03a1")
        buf.write("\u039f\3\2\2\2\u03a1\u03a2\3\2\2\2\u03a2K\3\2\2\2\u03a3")
        buf.write("\u03a1\3\2\2\2\u03a4\u03a5\b\'\1\2\u03a5\u03a6\5J&\2\u03a6")
        buf.write("\u03ac\3\2\2\2\u03a7\u03a8\f\3\2\2\u03a8\u03a9\7_\2\2")
        buf.write("\u03a9\u03ab\5J&\2\u03aa\u03a7\3\2\2\2\u03ab\u03ae\3\2")
        buf.write("\2\2\u03ac\u03aa\3\2\2\2\u03ac\u03ad\3\2\2\2\u03adM\3")
        buf.write("\2\2\2\u03ae\u03ac\3\2\2\2\u03af\u03b0\b(\1\2\u03b0\u03b1")
        buf.write("\5L\'\2\u03b1\u03b7\3\2\2\2\u03b2\u03b3\f\3\2\2\u03b3")
        buf.write("\u03b4\7s\2\2\u03b4\u03b6\5L\'\2\u03b5\u03b2\3\2\2\2\u03b6")
        buf.write("\u03b9\3\2\2\2\u03b7\u03b5\3\2\2\2\u03b7\u03b8\3\2\2\2")
        buf.write("\u03b8O\3\2\2\2\u03b9\u03b7\3\2\2\2\u03ba\u03bb\b)\1\2")
        buf.write("\u03bb\u03bc\5N(\2\u03bc\u03c2\3\2\2\2\u03bd\u03be\f\3")
        buf.write("\2\2\u03be\u03bf\7t\2\2\u03bf\u03c1\5N(\2\u03c0\u03bd")
        buf.write("\3\2\2\2\u03c1\u03c4\3\2\2\2\u03c2\u03c0\3\2\2\2\u03c2")
        buf.write("\u03c3\3\2\2\2\u03c3Q\3\2\2\2\u03c4\u03c2\3\2\2\2\u03c5")
        buf.write("\u03cd\5P)\2\u03c6\u03c7\5P)\2\u03c7\u03c8\7z\2\2\u03c8")
        buf.write("\u03c9\5\\/\2\u03c9\u03ca\7{\2\2\u03ca\u03cb\5T+\2\u03cb")
        buf.write("\u03cd\3\2\2\2\u03cc\u03c5\3\2\2\2\u03cc\u03c6\3\2\2\2")
        buf.write("\u03cdS\3\2\2\2\u03ce\u03d5\5R*\2\u03cf\u03d0\5P)\2\u03d0")
        buf.write("\u03d1\5Z.\2\u03d1\u03d2\5\u012c\u0097\2\u03d2\u03d5\3")
        buf.write("\2\2\2\u03d3\u03d5\5\u018c\u00c7\2\u03d4\u03ce\3\2\2\2")
        buf.write("\u03d4\u03cf\3\2\2\2\u03d4\u03d3\3\2\2\2\u03d5U\3\2\2")
        buf.write("\2\u03d6\u03d9\5T+\2\u03d7\u03d9\5X-\2\u03d8\u03d6\3\2")
        buf.write("\2\2\u03d8\u03d7\3\2\2\2\u03d9W\3\2\2\2\u03da\u03db\7")
        buf.write("\26\2\2\u03db\u03df\5T+\2\u03dc\u03dd\7\26\2\2\u03dd\u03df")
        buf.write("\5\u0130\u0099\2\u03de\u03da\3\2\2\2\u03de\u03dc\3\2\2")
        buf.write("\2\u03dfY\3\2\2\2\u03e0\u03ec\7b\2\2\u03e1\u03ec\7g\2")
        buf.write("\2\u03e2\u03ec\7h\2\2\u03e3\u03ec\7i\2\2\u03e4\u03ec\7")
        buf.write("e\2\2\u03e5\u03ec\7f\2\2\u03e6\u03ec\5\u0198\u00cd\2\u03e7")
        buf.write("\u03ec\7n\2\2\u03e8\u03ec\7k\2\2\u03e9\u03ec\7j\2\2\u03ea")
        buf.write("\u03ec\7l\2\2\u03eb\u03e0\3\2\2\2\u03eb\u03e1\3\2\2\2")
        buf.write("\u03eb\u03e2\3\2\2\2\u03eb\u03e3\3\2\2\2\u03eb\u03e4\3")
        buf.write("\2\2\2\u03eb\u03e5\3\2\2\2\u03eb\u03e6\3\2\2\2\u03eb\u03e7")
        buf.write("\3\2\2\2\u03eb\u03e8\3\2\2\2\u03eb\u03e9\3\2\2\2\u03eb")
        buf.write("\u03ea\3\2\2\2\u03ec[\3\2\2\2\u03ed\u03ee\b/\1\2\u03ee")
        buf.write("\u03ef\5T+\2\u03ef\u03f5\3\2\2\2\u03f0\u03f1\f\3\2\2\u03f1")
        buf.write("\u03f2\7w\2\2\u03f2\u03f4\5T+\2\u03f3\u03f0\3\2\2\2\u03f4")
        buf.write("\u03f7\3\2\2\2\u03f5\u03f3\3\2\2\2\u03f5\u03f6\3\2\2\2")
        buf.write("\u03f6]\3\2\2\2\u03f7\u03f5\3\2\2\2\u03f8\u03f9\b\60\1")
        buf.write("\2\u03f9\u03fa\5V,\2\u03fa\u0400\3\2\2\2\u03fb\u03fc\f")
        buf.write("\3\2\2\u03fc\u03fd\7w\2\2\u03fd\u03ff\5V,\2\u03fe\u03fb")
        buf.write("\3\2\2\2\u03ff\u0402\3\2\2\2\u0400\u03fe\3\2\2\2\u0400")
        buf.write("\u0401\3\2\2\2\u0401_\3\2\2\2\u0402\u0400\3\2\2\2\u0403")
        buf.write("\u0404\5R*\2\u0404a\3\2\2\2\u0405\u0420\5f\64\2\u0406")
        buf.write("\u0408\5\u00e0q\2\u0407\u0406\3\2\2\2\u0407\u0408\3\2")
        buf.write("\2\2\u0408\u0409\3\2\2\2\u0409\u0420\5h\65\2\u040a\u040c")
        buf.write("\5\u00e0q\2\u040b\u040a\3\2\2\2\u040b\u040c\3\2\2\2\u040c")
        buf.write("\u040d\3\2\2\2\u040d\u0420\5l\67\2\u040e\u0410\5\u00e0")
        buf.write("q\2\u040f\u040e\3\2\2\2\u040f\u0410\3\2\2\2\u0410\u0411")
        buf.write("\3\2\2\2\u0411\u0420\5t;\2\u0412\u0414\5\u00e0q\2\u0413")
        buf.write("\u0412\3\2\2\2\u0413\u0414\3\2\2\2\u0414\u0415\3\2\2\2")
        buf.write("\u0415\u0420\5x=\2\u0416\u0418\5\u00e0q\2\u0417\u0416")
        buf.write("\3\2\2\2\u0417\u0418\3\2\2\2\u0418\u0419\3\2\2\2\u0419")
        buf.write("\u0420\5\u0080A\2\u041a\u0420\5\u0084C\2\u041b\u041d\5")
        buf.write("\u00e0q\2\u041c\u041b\3\2\2\2\u041c\u041d\3\2\2\2\u041d")
        buf.write("\u041e\3\2\2\2\u041e\u0420\5\u0182\u00c2\2\u041f\u0405")
        buf.write("\3\2\2\2\u041f\u0407\3\2\2\2\u041f\u040b\3\2\2\2\u041f")
        buf.write("\u040f\3\2\2\2\u041f\u0413\3\2\2\2\u041f\u0417\3\2\2\2")
        buf.write("\u041f\u041a\3\2\2\2\u041f\u041c\3\2\2\2\u0420c\3\2\2")
        buf.write("\2\u0421\u0425\5b\62\2\u0422\u0425\5j\66\2\u0423\u0425")
        buf.write("\5\u0082B\2\u0424\u0421\3\2\2\2\u0424\u0422\3\2\2\2\u0424")
        buf.write("\u0423\3\2\2\2\u0425e\3\2\2\2\u0426\u0428\5\u00e0q\2\u0427")
        buf.write("\u0426\3\2\2\2\u0427\u0428\3\2\2\2\u0428\u0429\3\2\2\2")
        buf.write("\u0429\u042a\7\u0081\2\2\u042a\u042b\7{\2\2\u042b\u043b")
        buf.write("\5b\62\2\u042c\u042e\5\u00e0q\2\u042d\u042c\3\2\2\2\u042d")
        buf.write("\u042e\3\2\2\2\u042e\u042f\3\2\2\2\u042f\u0430\7\13\2")
        buf.write("\2\u0430\u0431\5`\61\2\u0431\u0432\7{\2\2\u0432\u0433")
        buf.write("\5b\62\2\u0433\u043b\3\2\2\2\u0434\u0436\5\u00e0q\2\u0435")
        buf.write("\u0434\3\2\2\2\u0435\u0436\3\2\2\2\u0436\u0437\3\2\2\2")
        buf.write("\u0437\u0438\7\30\2\2\u0438\u0439\7{\2\2\u0439\u043b\5")
        buf.write("b\62\2\u043a\u0427\3\2\2\2\u043a\u042d\3\2\2\2\u043a\u0435")
        buf.write("\3\2\2\2\u043bg\3\2\2\2\u043c\u043e\5\\/\2\u043d\u043c")
        buf.write("\3\2\2\2\u043d\u043e\3\2\2\2\u043e\u043f\3\2\2\2\u043f")
        buf.write("\u0440\7}\2\2\u0440i\3\2\2\2\u0441\u0443\5^\60\2\u0442")
        buf.write("\u0441\3\2\2\2\u0442\u0443\3\2\2\2\u0443\u0444\3\2\2\2")
        buf.write("\u0444\u0445\7}\2\2\u0445k\3\2\2\2\u0446\u0448\7V\2\2")
        buf.write("\u0447\u0449\5p9\2\u0448\u0447\3\2\2\2\u0448\u0449\3\2")
        buf.write("\2\2\u0449\u044a\3\2\2\2\u044a\u044b\7W\2\2\u044bm\3\2")
        buf.write("\2\2\u044c\u044e\7V\2\2\u044d\u044f\5r:\2\u044e\u044d")
        buf.write("\3\2\2\2\u044e\u044f\3\2\2\2\u044f\u0450\3\2\2\2\u0450")
        buf.write("\u0451\7W\2\2\u0451o\3\2\2\2\u0452\u0453\b9\1\2\u0453")
        buf.write("\u0454\5b\62\2\u0454\u0459\3\2\2\2\u0455\u0456\f\3\2\2")
        buf.write("\u0456\u0458\5b\62\2\u0457\u0455\3\2\2\2\u0458\u045b\3")
        buf.write("\2\2\2\u0459\u0457\3\2\2\2\u0459\u045a\3\2\2\2\u045aq")
        buf.write("\3\2\2\2\u045b\u0459\3\2\2\2\u045c\u045d\b:\1\2\u045d")
        buf.write("\u045e\5d\63\2\u045e\u0463\3\2\2\2\u045f\u0460\f\3\2\2")
        buf.write("\u0460\u0462\5d\63\2\u0461\u045f\3\2\2\2\u0462\u0465\3")
        buf.write("\2\2\2\u0463\u0461\3\2\2\2\u0463\u0464\3\2\2\2\u0464s")
        buf.write("\3\2\2\2\u0465\u0463\3\2\2\2\u0466\u0467\7(\2\2\u0467")
        buf.write("\u0468\7R\2\2\u0468\u0469\5v<\2\u0469\u046a\7S\2\2\u046a")
        buf.write("\u046b\5b\62\2\u046b\u047b\3\2\2\2\u046c\u046d\7(\2\2")
        buf.write("\u046d\u046e\7R\2\2\u046e\u046f\5v<\2\u046f\u0470\7S\2")
        buf.write("\2\u0470\u0471\5b\62\2\u0471\u0472\7\35\2\2\u0472\u0473")
        buf.write("\5b\62\2\u0473\u047b\3\2\2\2\u0474\u0475\7@\2\2\u0475")
        buf.write("\u0476\7R\2\2\u0476\u0477\5v<\2\u0477\u0478\7S\2\2\u0478")
        buf.write("\u0479\5b\62\2\u0479\u047b\3\2\2\2\u047a\u0466\3\2\2\2")
        buf.write("\u047a\u046c\3\2\2\2\u047a\u0474\3\2\2\2\u047bu\3\2\2")
        buf.write("\2\u047c\u048d\5\\/\2\u047d\u047f\5\u00e0q\2\u047e\u047d")
        buf.write("\3\2\2\2\u047e\u047f\3\2\2\2\u047f\u0480\3\2\2\2\u0480")
        buf.write("\u0481\5\u0098M\2\u0481\u0482\5\u00fa~\2\u0482\u0483\7")
        buf.write("b\2\2\u0483\u0484\5\u012c\u0097\2\u0484\u048d\3\2\2\2")
        buf.write("\u0485\u0487\5\u00e0q\2\u0486\u0485\3\2\2\2\u0486\u0487")
        buf.write("\3\2\2\2\u0487\u0488\3\2\2\2\u0488\u0489\5\u0098M\2\u0489")
        buf.write("\u048a\5\u00fa~\2\u048a\u048b\5\u0130\u0099\2\u048b\u048d")
        buf.write("\3\2\2\2\u048c\u047c\3\2\2\2\u048c\u047e\3\2\2\2\u048c")
        buf.write("\u0486\3\2\2\2\u048dw\3\2\2\2\u048e\u048f\7Q\2\2\u048f")
        buf.write("\u0490\7R\2\2\u0490\u0491\5v<\2\u0491\u0492\7S\2\2\u0492")
        buf.write("\u0493\5b\62\2\u0493\u04b2\3\2\2\2\u0494\u0495\7\32\2")
        buf.write("\2\u0495\u0496\5b\62\2\u0496\u0497\7Q\2\2\u0497\u0498")
        buf.write("\7R\2\2\u0498\u0499\5\\/\2\u0499\u049a\7S\2\2\u049a\u049b")
        buf.write("\7}\2\2\u049b\u04b2\3\2\2\2\u049c\u049d\7%\2\2\u049d\u049e")
        buf.write("\7R\2\2\u049e\u04a0\5z>\2\u049f\u04a1\5v<\2\u04a0\u049f")
        buf.write("\3\2\2\2\u04a0\u04a1\3\2\2\2\u04a1\u04a2\3\2\2\2\u04a2")
        buf.write("\u04a4\7}\2\2\u04a3\u04a5\5\\/\2\u04a4\u04a3\3\2\2\2\u04a4")
        buf.write("\u04a5\3\2\2\2\u04a5\u04a6\3\2\2\2\u04a6\u04a7\7S\2\2")
        buf.write("\u04a7\u04a8\5b\62\2\u04a8\u04b2\3\2\2\2\u04a9\u04aa\7")
        buf.write("%\2\2\u04aa\u04ab\7R\2\2\u04ab\u04ac\5|?\2\u04ac\u04ad")
        buf.write("\7{\2\2\u04ad\u04ae\5~@\2\u04ae\u04af\7S\2\2\u04af\u04b0")
        buf.write("\5b\62\2\u04b0\u04b2\3\2\2\2\u04b1\u048e\3\2\2\2\u04b1")
        buf.write("\u0494\3\2\2\2\u04b1\u049c\3\2\2\2\u04b1\u04a9\3\2\2\2")
        buf.write("\u04b2y\3\2\2\2\u04b3\u04b6\5h\65\2\u04b4\u04b6\5\u008e")
        buf.write("H\2\u04b5\u04b3\3\2\2\2\u04b5\u04b4\3\2\2\2\u04b6{\3\2")
        buf.write("\2\2\u04b7\u04b9\5\u00e0q\2\u04b8\u04b7\3\2\2\2\u04b8")
        buf.write("\u04b9\3\2\2\2\u04b9\u04ba\3\2\2\2\u04ba\u04bb\5\u0098")
        buf.write("M\2\u04bb\u04bc\5\u00fa~\2\u04bc}\3\2\2\2\u04bd\u04c0")
        buf.write("\5\\/\2\u04be\u04c0\5\u0130\u0099\2\u04bf\u04bd\3\2\2")
        buf.write("\2\u04bf\u04be\3\2\2\2\u04c0\177\3\2\2\2\u04c1\u04c2\7")
        buf.write("\n\2\2\u04c2\u04d2\7}\2\2\u04c3\u04c4\7\24\2\2\u04c4\u04d2")
        buf.write("\7}\2\2\u04c5\u04c7\78\2\2\u04c6\u04c8\5\\/\2\u04c7\u04c6")
        buf.write("\3\2\2\2\u04c7\u04c8\3\2\2\2\u04c8\u04c9\3\2\2\2\u04c9")
        buf.write("\u04d2\7}\2\2\u04ca\u04cb\78\2\2\u04cb\u04cc\5\u0130\u0099")
        buf.write("\2\u04cc\u04cd\7}\2\2\u04cd\u04d2\3\2\2\2\u04ce\u04cf")
        buf.write("\7\'\2\2\u04cf\u04d0\7\u0081\2\2\u04d0\u04d2\7}\2\2\u04d1")
        buf.write("\u04c1\3\2\2\2\u04d1\u04c3\3\2\2\2\u04d1\u04c5\3\2\2\2")
        buf.write("\u04d1\u04ca\3\2\2\2\u04d1\u04ce\3\2\2\2\u04d2\u0081\3")
        buf.write("\2\2\2\u04d3\u04d5\7\25\2\2\u04d4\u04d6\5\\/\2\u04d5\u04d4")
        buf.write("\3\2\2\2\u04d5\u04d6\3\2\2\2\u04d6\u04d7\3\2\2\2\u04d7")
        buf.write("\u04de\7}\2\2\u04d8\u04d9\7\25\2\2\u04d9\u04da\5\u0130")
        buf.write("\u0099\2\u04da\u04db\7}\2\2\u04db\u04de\3\2\2\2\u04dc")
        buf.write("\u04de\5\u0080A\2\u04dd\u04d3\3\2\2\2\u04dd\u04d8\3\2")
        buf.write("\2\2\u04dd\u04dc\3\2\2\2\u04de\u0083\3\2\2\2\u04df\u04e0")
        buf.write("\5\u008aF\2\u04e0\u0085\3\2\2\2\u04e1\u04e2\bD\1\2\u04e2")
        buf.write("\u04e3\5\u0088E\2\u04e3\u04e8\3\2\2\2\u04e4\u04e5\f\3")
        buf.write("\2\2\u04e5\u04e7\5\u0088E\2\u04e6\u04e4\3\2\2\2\u04e7")
        buf.write("\u04ea\3\2\2\2\u04e8\u04e6\3\2\2\2\u04e8\u04e9\3\2\2\2")
        buf.write("\u04e9\u0087\3\2\2\2\u04ea\u04e8\3\2\2\2\u04eb\u04f6\5")
        buf.write("\u008aF\2\u04ec\u04f6\5\u0120\u0091\2\u04ed\u04f6\5\u0124")
        buf.write("\u0093\2\u04ee\u04f6\5\u016a\u00b6\2\u04ef\u04f6\5\u017e")
        buf.write("\u00c0\2\u04f0\u04f6\5\u0180\u00c1\2\u04f1\u04f6\5\u00de")
        buf.write("p\2\u04f2\u04f6\5\u00c6d\2\u04f3\u04f6\5\u0092J\2\u04f4")
        buf.write("\u04f6\5\u0094K\2\u04f5\u04eb\3\2\2\2\u04f5\u04ec\3\2")
        buf.write("\2\2\u04f5\u04ed\3\2\2\2\u04f5\u04ee\3\2\2\2\u04f5\u04ef")
        buf.write("\3\2\2\2\u04f5\u04f0\3\2\2\2\u04f5\u04f1\3\2\2\2\u04f5")
        buf.write("\u04f2\3\2\2\2\u04f5\u04f3\3\2\2\2\u04f5\u04f4\3\2\2\2")
        buf.write("\u04f6\u0089\3\2\2\2\u04f7\u0500\5\u008eH\2\u04f8\u0500")
        buf.write("\5\u00dco\2\u04f9\u0500\5\u00d4k\2\u04fa\u0500\5\u00d8")
        buf.write("m\2\u04fb\u0500\5\u00dan\2\u04fc\u0500\5\u0090I\2\u04fd")
        buf.write("\u0500\5\u008cG\2\u04fe\u0500\5\u00b6\\\2\u04ff\u04f7")
        buf.write("\3\2\2\2\u04ff\u04f8\3\2\2\2\u04ff\u04f9\3\2\2\2\u04ff")
        buf.write("\u04fa\3\2\2\2\u04ff\u04fb\3\2\2\2\u04ff\u04fc\3\2\2\2")
        buf.write("\u04ff\u04fd\3\2\2\2\u04ff\u04fe\3\2\2\2\u0500\u008b\3")
        buf.write("\2\2\2\u0501\u0502\7L\2\2\u0502\u0504\7\u0081\2\2\u0503")
        buf.write("\u0505\5\u00e0q\2\u0504\u0503\3\2\2\2\u0504\u0505\3\2")
        buf.write("\2\2\u0505\u0506\3\2\2\2\u0506\u0507\7b\2\2\u0507\u0508")
        buf.write("\5\u010e\u0088\2\u0508\u0509\7}\2\2\u0509\u008d\3\2\2")
        buf.write("\2\u050a\u050c\5\u0098M\2\u050b\u050a\3\2\2\2\u050b\u050c")
        buf.write("\3\2\2\2\u050c\u050e\3\2\2\2\u050d\u050f\5\u00f6|\2\u050e")
        buf.write("\u050d\3\2\2\2\u050e\u050f\3\2\2\2\u050f\u0510\3\2\2\2")
        buf.write("\u0510\u0519\7}\2\2\u0511\u0513\5\u00e0q\2\u0512\u0514")
        buf.write("\5\u0098M\2\u0513\u0512\3\2\2\2\u0513\u0514\3\2\2\2\u0514")
        buf.write("\u0515\3\2\2\2\u0515\u0516\5\u00f6|\2\u0516\u0517\7}\2")
        buf.write("\2\u0517\u0519\3\2\2\2\u0518\u050b\3\2\2\2\u0518\u0511")
        buf.write("\3\2\2\2\u0519\u008f\3\2\2\2\u051a\u051b\7=\2\2\u051b")
        buf.write("\u051c\7R\2\2\u051c\u051d\5`\61\2\u051d\u051e\7w\2\2\u051e")
        buf.write("\u051f\7\u008a\2\2\u051f\u0520\7S\2\2\u0520\u0521\7}\2")
        buf.write("\2\u0521\u0091\3\2\2\2\u0522\u0523\7}\2\2\u0523\u0093")
        buf.write("\3\2\2\2\u0524\u0525\5\u00e0q\2\u0525\u0526\7}\2\2\u0526")
        buf.write("\u0095\3\2\2\2\u0527\u052e\5\u009aN\2\u0528\u052e\5\u00a0")
        buf.write("Q\2\u0529\u052e\5\u009cO\2\u052a\u052e\7&\2\2\u052b\u052e")
        buf.write("\7G\2\2\u052c\u052e\7\22\2\2\u052d\u0527\3\2\2\2\u052d")
        buf.write("\u0528\3\2\2\2\u052d\u0529\3\2\2\2\u052d\u052a\3\2\2\2")
        buf.write("\u052d\u052b\3\2\2\2\u052d\u052c\3\2\2\2\u052e\u0097\3")
        buf.write("\2\2\2\u052f\u0531\5\u0096L\2\u0530\u0532\5\u00e0q\2\u0531")
        buf.write("\u0530\3\2\2\2\u0531\u0532\3\2\2\2\u0532\u0537\3\2\2\2")
        buf.write("\u0533\u0534\5\u0096L\2\u0534\u0535\5\u0098M\2\u0535\u0537")
        buf.write("\3\2\2\2\u0536\u052f\3\2\2\2\u0536\u0533\3\2\2\2\u0537")
        buf.write("\u0099\3\2\2\2\u0538\u0539\t\4\2\2\u0539\u009b\3\2\2\2")
        buf.write("\u053a\u053b\t\5\2\2\u053b\u009d\3\2\2\2\u053c\u053d\7")
        buf.write("\u0081\2\2\u053d\u009f\3\2\2\2\u053e\u0542\5\u00a2R\2")
        buf.write("\u053f\u0542\5\u0134\u009b\2\u0540\u0542\5\u00b2Z\2\u0541")
        buf.write("\u053e\3\2\2\2\u0541\u053f\3\2\2\2\u0541\u0540\3\2\2\2")
        buf.write("\u0542\u00a1\3\2\2\2\u0543\u0548\5\u00a8U\2\u0544\u0548")
        buf.write("\5\u00aeX\2\u0545\u0548\5\u017c\u00bf\2\u0546\u0548\5")
        buf.write("\u0108\u0085\2\u0547\u0543\3\2\2\2\u0547\u0544\3\2\2\2")
        buf.write("\u0547\u0545\3\2\2\2\u0547\u0546\3\2\2\2\u0548\u00a3\3")
        buf.write("\2\2\2\u0549\u054b\5\u00a0Q\2\u054a\u054c\5\u00e0q\2\u054b")
        buf.write("\u054a\3\2\2\2\u054b\u054c\3\2\2\2\u054c\u0551\3\2\2\2")
        buf.write("\u054d\u054e\5\u00a0Q\2\u054e\u054f\5\u00a4S\2\u054f\u0551")
        buf.write("\3\2\2\2\u0550\u0549\3\2\2\2\u0550\u054d\3\2\2\2\u0551")
        buf.write("\u00a5\3\2\2\2\u0552\u0554\5\u00a2R\2\u0553\u0555\5\u00e0")
        buf.write("q\2\u0554\u0553\3\2\2\2\u0554\u0555\3\2\2\2\u0555\u055a")
        buf.write("\3\2\2\2\u0556\u0557\5\u00a2R\2\u0557\u0558\5\u00a6T\2")
        buf.write("\u0558\u055a\3\2\2\2\u0559\u0552\3\2\2\2\u0559\u0556\3")
        buf.write("\2\2\2\u055a\u00a7\3\2\2\2\u055b\u055d\5\f\7\2\u055c\u055b")
        buf.write("\3\2\2\2\u055c\u055d\3\2\2\2\u055d\u055e\3\2\2\2\u055e")
        buf.write("\u0573\5\u00aaV\2\u055f\u0560\5\f\7\2\u0560\u0561\7A\2")
        buf.write("\2\u0561\u0562\5\u0172\u00ba\2\u0562\u0573\3\2\2\2\u0563")
        buf.write("\u0573\7\r\2\2\u0564\u0573\7\16\2\2\u0565\u0573\7\17\2")
        buf.write("\2\u0566\u0573\7P\2\2\u0567\u0573\7\t\2\2\u0568\u0573")
        buf.write("\79\2\2\u0569\u0573\7*\2\2\u056a\u0573\7+\2\2\u056b\u0573")
        buf.write("\7:\2\2\u056c\u0573\7K\2\2\u056d\u0573\7$\2\2\u056e\u0573")
        buf.write("\7\33\2\2\u056f\u0573\7N\2\2\u0570\u0573\7\b\2\2\u0571")
        buf.write("\u0573\5\u00acW\2\u0572\u055c\3\2\2\2\u0572\u055f\3\2")
        buf.write("\2\2\u0572\u0563\3\2\2\2\u0572\u0564\3\2\2\2\u0572\u0565")
        buf.write("\3\2\2\2\u0572\u0566\3\2\2\2\u0572\u0567\3\2\2\2\u0572")
        buf.write("\u0568\3\2\2\2\u0572\u0569\3\2\2\2\u0572\u056a\3\2\2\2")
        buf.write("\u0572\u056b\3\2\2\2\u0572\u056c\3\2\2\2\u0572\u056d\3")
        buf.write("\2\2\2\u0572\u056e\3\2\2\2\u0572\u056f\3\2\2\2\u0572\u0570")
        buf.write("\3\2\2\2\u0572\u0571\3\2\2\2\u0573\u00a9\3\2\2\2\u0574")
        buf.write("\u0579\5\u0132\u009a\2\u0575\u0579\5\u00b0Y\2\u0576\u0579")
        buf.write("\5\u009eP\2\u0577\u0579\5\u0172\u00ba\2\u0578\u0574\3")
        buf.write("\2\2\2\u0578\u0575\3\2\2\2\u0578\u0576\3\2\2\2\u0578\u0577")
        buf.write("\3\2\2\2\u0579\u00ab\3\2\2\2\u057a\u057b\7\27\2\2\u057b")
        buf.write("\u057c\7R\2\2\u057c\u057d\5\\/\2\u057d\u057e\7S\2\2\u057e")
        buf.write("\u0584\3\2\2\2\u057f\u0580\7\27\2\2\u0580\u0581\7R\2\2")
        buf.write("\u0581\u0582\7\b\2\2\u0582\u0584\7S\2\2\u0583\u057a\3")
        buf.write("\2\2\2\u0583\u057f\3\2\2\2\u0584\u00ad\3\2\2\2\u0585\u0587")
        buf.write("\5\u013c\u009f\2\u0586\u0588\5\u00e0q\2\u0587\u0586\3")
        buf.write("\2\2\2\u0587\u0588\3\2\2\2\u0588\u058a\3\2\2\2\u0589\u058b")
        buf.write("\5\f\7\2\u058a\u0589\3\2\2\2\u058a\u058b\3\2\2\2\u058b")
        buf.write("\u058c\3\2\2\2\u058c\u058d\7\u0081\2\2\u058d\u059e\3\2")
        buf.write("\2\2\u058e\u058f\5\u013c\u009f\2\u058f\u0590\5\u0172\u00ba")
        buf.write("\2\u0590\u059e\3\2\2\2\u0591\u0592\5\u013c\u009f\2\u0592")
        buf.write("\u0594\5\f\7\2\u0593\u0595\7A\2\2\u0594\u0593\3\2\2\2")
        buf.write("\u0594\u0595\3\2\2\2\u0595\u0596\3\2\2\2\u0596\u0597\5")
        buf.write("\u0172\u00ba\2\u0597\u059e\3\2\2\2\u0598\u059a\7\36\2")
        buf.write("\2\u0599\u059b\5\f\7\2\u059a\u0599\3\2\2\2\u059a\u059b")
        buf.write("\3\2\2\2\u059b\u059c\3\2\2\2\u059c\u059e\7\u0081\2\2\u059d")
        buf.write("\u0585\3\2\2\2\u059d\u058e\3\2\2\2\u059d\u0591\3\2\2\2")
        buf.write("\u059d\u0598\3\2\2\2\u059e\u00af\3\2\2\2\u059f\u05a0\7")
        buf.write("\u0081\2\2\u05a0\u00b1\3\2\2\2\u05a1\u05a2\5\u00b4[\2")
        buf.write("\u05a2\u05a4\7V\2\2\u05a3\u05a5\5\u00bc_\2\u05a4\u05a3")
        buf.write("\3\2\2\2\u05a4\u05a5\3\2\2\2\u05a5\u05a6\3\2\2\2\u05a6")
        buf.write("\u05a7\7W\2\2\u05a7\u05af\3\2\2\2\u05a8\u05a9\5\u00b4")
        buf.write("[\2\u05a9\u05aa\7V\2\2\u05aa\u05ab\5\u00bc_\2\u05ab\u05ac")
        buf.write("\7w\2\2\u05ac\u05ad\7W\2\2\u05ad\u05af\3\2\2\2\u05ae\u05a1")
        buf.write("\3\2\2\2\u05ae\u05a8\3\2\2\2\u05af\u00b3\3\2\2\2\u05b0")
        buf.write("\u05b2\5\u00b8]\2\u05b1\u05b3\5\u00e0q\2\u05b2\u05b1\3")
        buf.write("\2\2\2\u05b2\u05b3\3\2\2\2\u05b3\u05b5\3\2\2\2\u05b4\u05b6")
        buf.write("\7\u0081\2\2\u05b5\u05b4\3\2\2\2\u05b5\u05b6\3\2\2\2\u05b6")
        buf.write("\u05b8\3\2\2\2\u05b7\u05b9\5\u00ba^\2\u05b8\u05b7\3\2")
        buf.write("\2\2\u05b8\u05b9\3\2\2\2\u05b9\u05c4\3\2\2\2\u05ba\u05bc")
        buf.write("\5\u00b8]\2\u05bb\u05bd\5\u00e0q\2\u05bc\u05bb\3\2\2\2")
        buf.write("\u05bc\u05bd\3\2\2\2\u05bd\u05be\3\2\2\2\u05be\u05bf\5")
        buf.write("\f\7\2\u05bf\u05c1\7\u0081\2\2\u05c0\u05c2\5\u00ba^\2")
        buf.write("\u05c1\u05c0\3\2\2\2\u05c1\u05c2\3\2\2\2\u05c2\u05c4\3")
        buf.write("\2\2\2\u05c3\u05b0\3\2\2\2\u05c3\u05ba\3\2\2\2\u05c4\u00b5")
        buf.write("\3\2\2\2\u05c5\u05c7\5\u00b8]\2\u05c6\u05c8\5\u00e0q\2")
        buf.write("\u05c7\u05c6\3\2\2\2\u05c7\u05c8\3\2\2\2\u05c8\u05c9\3")
        buf.write("\2\2\2\u05c9\u05cb\7\u0081\2\2\u05ca\u05cc\5\u00ba^\2")
        buf.write("\u05cb\u05ca\3\2\2\2\u05cb\u05cc\3\2\2\2\u05cc\u05cd\3")
        buf.write("\2\2\2\u05cd\u05ce\7}\2\2\u05ce\u00b7\3\2\2\2\u05cf\u05d5")
        buf.write("\7\36\2\2\u05d0\u05d1\7\36\2\2\u05d1\u05d5\7\20\2\2\u05d2")
        buf.write("\u05d3\7\36\2\2\u05d3\u05d5\7?\2\2\u05d4\u05cf\3\2\2\2")
        buf.write("\u05d4\u05d0\3\2\2\2\u05d4\u05d2\3\2\2\2\u05d5\u00b9\3")
        buf.write("\2\2\2\u05d6\u05d7\7{\2\2\u05d7\u05d8\5\u00a4S\2\u05d8")
        buf.write("\u00bb\3\2\2\2\u05d9\u05da\b_\1\2\u05da\u05db\5\u00be")
        buf.write("`\2\u05db\u05e1\3\2\2\2\u05dc\u05dd\f\3\2\2\u05dd\u05de")
        buf.write("\7w\2\2\u05de\u05e0\5\u00be`\2\u05df\u05dc\3\2\2\2\u05e0")
        buf.write("\u05e3\3\2\2\2\u05e1\u05df\3\2\2\2\u05e1\u05e2\3\2\2\2")
        buf.write("\u05e2\u00bd\3\2\2\2\u05e3\u05e1\3\2\2\2\u05e4\u05ea\5")
        buf.write("\u00c0a\2\u05e5\u05e6\5\u00c0a\2\u05e6\u05e7\7b\2\2\u05e7")
        buf.write("\u05e8\5`\61\2\u05e8\u05ea\3\2\2\2\u05e9\u05e4\3\2\2\2")
        buf.write("\u05e9\u05e5\3\2\2\2\u05ea\u00bf\3\2\2\2\u05eb\u05ec\7")
        buf.write("\u0081\2\2\u05ec\u00c1\3\2\2\2\u05ed\u05f0\5\u00c4c\2")
        buf.write("\u05ee\u05f0\5\u00d2j\2\u05ef\u05ed\3\2\2\2\u05ef\u05ee")
        buf.write("\3\2\2\2\u05f0\u00c3\3\2\2\2\u05f1\u05f2\7\u0081\2\2\u05f2")
        buf.write("\u00c5\3\2\2\2\u05f3\u05f6\5\u00c8e\2\u05f4\u05f6\5\u00ce")
        buf.write("h\2\u05f5\u05f3\3\2\2\2\u05f5\u05f4\3\2\2\2\u05f6\u00c7")
        buf.write("\3\2\2\2\u05f7\u05fa\5\u00caf\2\u05f8\u05fa\5\u00ccg\2")
        buf.write("\u05f9\u05f7\3\2\2\2\u05f9\u05f8\3\2\2\2\u05fa\u00c9\3")
        buf.write("\2\2\2\u05fb\u05fd\7)\2\2\u05fc\u05fb\3\2\2\2\u05fc\u05fd")
        buf.write("\3\2\2\2\u05fd\u05fe\3\2\2\2\u05fe\u05ff\7-\2\2\u05ff")
        buf.write("\u0600\7\u0081\2\2\u0600\u0601\7V\2\2\u0601\u0602\5\u00d0")
        buf.write("i\2\u0602\u0603\7W\2\2\u0603\u00cb\3\2\2\2\u0604\u0606")
        buf.write("\7)\2\2\u0605\u0604\3\2\2\2\u0605\u0606\3\2\2\2\u0606")
        buf.write("\u0607\3\2\2\2\u0607\u0608\7-\2\2\u0608\u0609\5\u00c4")
        buf.write("c\2\u0609\u060a\7V\2\2\u060a\u060b\5\u00d0i\2\u060b\u060c")
        buf.write("\7W\2\2\u060c\u00cd\3\2\2\2\u060d\u060f\7)\2\2\u060e\u060d")
        buf.write("\3\2\2\2\u060e\u060f\3\2\2\2\u060f\u0610\3\2\2\2\u0610")
        buf.write("\u0611\7-\2\2\u0611\u0612\7V\2\2\u0612\u0613\5\u00d0i")
        buf.write("\2\u0613\u0614\7W\2\2\u0614\u00cf\3\2\2\2\u0615\u0617")
        buf.write("\5\u0086D\2\u0616\u0615\3\2\2\2\u0616\u0617\3\2\2\2\u0617")
        buf.write("\u00d1\3\2\2\2\u0618\u0619\7\u0081\2\2\u0619\u00d3\3\2")
        buf.write("\2\2\u061a\u061b\7-\2\2\u061b\u061c\7\u0081\2\2\u061c")
        buf.write("\u061d\7b\2\2\u061d\u061e\5\u00d6l\2\u061e\u061f\7}\2")
        buf.write("\2\u061f\u00d5\3\2\2\2\u0620\u0622\5\f\7\2\u0621\u0620")
        buf.write("\3\2\2\2\u0621\u0622\3\2\2\2\u0622\u0623\3\2\2\2\u0623")
        buf.write("\u0624\5\u00c2b\2\u0624\u00d7\3\2\2\2\u0625\u0627\7L\2")
        buf.write("\2\u0626\u0628\7I\2\2\u0627\u0626\3\2\2\2\u0627\u0628")
        buf.write("\3\2\2\2\u0628\u0629\3\2\2\2\u0629\u062a\5\f\7\2\u062a")
        buf.write("\u062b\5\b\5\2\u062b\u062c\7}\2\2\u062c\u0633\3\2\2\2")
        buf.write("\u062d\u062e\7L\2\2\u062e\u062f\7|\2\2\u062f\u0630\5\b")
        buf.write("\5\2\u0630\u0631\7}\2\2\u0631\u0633\3\2\2\2\u0632\u0625")
        buf.write("\3\2\2\2\u0632\u062d\3\2\2\2\u0633\u00d9\3\2\2\2\u0634")
        buf.write("\u0636\5\u00e0q\2\u0635\u0634\3\2\2\2\u0635\u0636\3\2")
        buf.write("\2\2\u0636\u0637\3\2\2\2\u0637\u0638\7L\2\2\u0638\u063a")
        buf.write("\7-\2\2\u0639\u063b\5\f\7\2\u063a\u0639\3\2\2\2\u063a")
        buf.write("\u063b\3\2\2\2\u063b\u063c\3\2\2\2\u063c\u063d\5\u00c2")
        buf.write("b\2\u063d\u063e\7}\2\2\u063e\u00db\3\2\2\2\u063f\u0640")
        buf.write("\7\7\2\2\u0640\u0641\7R\2\2\u0641\u0642\7\u008a\2\2\u0642")
        buf.write("\u0643\7S\2\2\u0643\u0644\7}\2\2\u0644\u00dd\3\2\2\2\u0645")
        buf.write("\u0646\7!\2\2\u0646\u0647\7\u008a\2\2\u0647\u0649\7V\2")
        buf.write("\2\u0648\u064a\5\u0086D\2\u0649\u0648\3\2\2\2\u0649\u064a")
        buf.write("\3\2\2\2\u064a\u064b\3\2\2\2\u064b\u0650\7W\2\2\u064c")
        buf.write("\u064d\7!\2\2\u064d\u064e\7\u008a\2\2\u064e\u0650\5\u0088")
        buf.write("E\2\u064f\u0645\3\2\2\2\u064f\u064c\3\2\2\2\u0650\u00df")
        buf.write("\3\2\2\2\u0651\u0652\bq\1\2\u0652\u0653\5\u00e2r\2\u0653")
        buf.write("\u0658\3\2\2\2\u0654\u0655\f\3\2\2\u0655\u0657\5\u00e2")
        buf.write("r\2\u0656\u0654\3\2\2\2\u0657\u065a\3\2\2\2\u0658\u0656")
        buf.write("\3\2\2\2\u0658\u0659\3\2\2\2\u0659\u00e1\3\2\2\2\u065a")
        buf.write("\u0658\3\2\2\2\u065b\u065c\7T\2\2\u065c\u065d\7T\2\2\u065d")
        buf.write("\u065e\5\u00e6t\2\u065e\u065f\7U\2\2\u065f\u0660\7U\2")
        buf.write("\2\u0660\u0663\3\2\2\2\u0661\u0663\5\u00e4s\2\u0662\u065b")
        buf.write("\3\2\2\2\u0662\u0661\3\2\2\2\u0663\u00e3\3\2\2\2\u0664")
        buf.write("\u0665\7\5\2\2\u0665\u0666\7R\2\2\u0666\u0668\5\u010e")
        buf.write("\u0088\2\u0667\u0669\7\u0080\2\2\u0668\u0667\3\2\2\2\u0668")
        buf.write("\u0669\3\2\2\2\u0669\u066a\3\2\2\2\u066a\u066b\7S\2\2")
        buf.write("\u066b\u0675\3\2\2\2\u066c\u066d\7\5\2\2\u066d\u066e\7")
        buf.write("R\2\2\u066e\u0670\5`\61\2\u066f\u0671\7\u0080\2\2\u0670")
        buf.write("\u066f\3\2\2\2\u0670\u0671\3\2\2\2\u0671\u0672\3\2\2\2")
        buf.write("\u0672\u0673\7S\2\2\u0673\u0675\3\2\2\2\u0674\u0664\3")
        buf.write("\2\2\2\u0674\u066c\3\2\2\2\u0675\u00e5\3\2\2\2\u0676\u0678")
        buf.write("\bt\1\2\u0677\u0679\5\u00e8u\2\u0678\u0677\3\2\2\2\u0678")
        buf.write("\u0679\3\2\2\2\u0679\u067e\3\2\2\2\u067a\u067b\5\u00e8")
        buf.write("u\2\u067b\u067c\7\u0080\2\2\u067c\u067e\3\2\2\2\u067d")
        buf.write("\u0676\3\2\2\2\u067d\u067a\3\2\2\2\u067e\u068b\3\2\2\2")
        buf.write("\u067f\u0680\f\5\2\2\u0680\u0682\7w\2\2\u0681\u0683\5")
        buf.write("\u00e8u\2\u0682\u0681\3\2\2\2\u0682\u0683\3\2\2\2\u0683")
        buf.write("\u068a\3\2\2\2\u0684\u0685\f\3\2\2\u0685\u0686\7w\2\2")
        buf.write("\u0686\u0687\5\u00e8u\2\u0687\u0688\7\u0080\2\2\u0688")
        buf.write("\u068a\3\2\2\2\u0689\u067f\3\2\2\2\u0689\u0684\3\2\2\2")
        buf.write("\u068a\u068d\3\2\2\2\u068b\u0689\3\2\2\2\u068b\u068c\3")
        buf.write("\2\2\2\u068c\u00e7\3\2\2\2\u068d\u068b\3\2\2\2\u068e\u0690")
        buf.write("\5\u00eav\2\u068f\u0691\5\u00f0y\2\u0690\u068f\3\2\2\2")
        buf.write("\u0690\u0691\3\2\2\2\u0691\u00e9\3\2\2\2\u0692\u0695\7")
        buf.write("\u0081\2\2\u0693\u0695\5\u00ecw\2\u0694\u0692\3\2\2\2")
        buf.write("\u0694\u0693\3\2\2\2\u0695\u00eb\3\2\2\2\u0696\u0697\5")
        buf.write("\u00eex\2\u0697\u0698\7|\2\2\u0698\u0699\7\u0081\2\2\u0699")
        buf.write("\u00ed\3\2\2\2\u069a\u069b\7\u0081\2\2\u069b\u00ef\3\2")
        buf.write("\2\2\u069c\u069d\7R\2\2\u069d\u069e\5\u00f2z\2\u069e\u069f")
        buf.write("\7S\2\2\u069f\u00f1\3\2\2\2\u06a0\u06a2\bz\1\2\u06a1\u06a3")
        buf.write("\5\u00f4{\2\u06a2\u06a1\3\2\2\2\u06a2\u06a3\3\2\2\2\u06a3")
        buf.write("\u06a8\3\2\2\2\u06a4\u06a5\f\3\2\2\u06a5\u06a7\5\u00f4")
        buf.write("{\2\u06a6\u06a4\3\2\2\2\u06a7\u06aa\3\2\2\2\u06a8\u06a6")
        buf.write("\3\2\2\2\u06a8\u06a9\3\2\2\2\u06a9\u00f3\3\2\2\2\u06aa")
        buf.write("\u06a8\3\2\2\2\u06ab\u06ac\7R\2\2\u06ac\u06ad\5\u00f2")
        buf.write("z\2\u06ad\u06ae\7S\2\2\u06ae\u06b8\3\2\2\2\u06af\u06b0")
        buf.write("\7T\2\2\u06b0\u06b1\5\u00f2z\2\u06b1\u06b2\7U\2\2\u06b2")
        buf.write("\u06b8\3\2\2\2\u06b3\u06b4\7V\2\2\u06b4\u06b5\5\u00f2")
        buf.write("z\2\u06b5\u06b6\7W\2\2\u06b6\u06b8\3\2\2\2\u06b7\u06ab")
        buf.write("\3\2\2\2\u06b7\u06af\3\2\2\2\u06b7\u06b3\3\2\2\2\u06b8")
        buf.write("\u00f5\3\2\2\2\u06b9\u06ba\b|\1\2\u06ba\u06bb\5\u00f8")
        buf.write("}\2\u06bb\u06c1\3\2\2\2\u06bc\u06bd\f\3\2\2\u06bd\u06be")
        buf.write("\7w\2\2\u06be\u06c0\5\u00f8}\2\u06bf\u06bc\3\2\2\2\u06c0")
        buf.write("\u06c3\3\2\2\2\u06c1\u06bf\3\2\2\2\u06c1\u06c2\3\2\2\2")
        buf.write("\u06c2\u00f7\3\2\2\2\u06c3\u06c1\3\2\2\2\u06c4\u06c6\5")
        buf.write("\u00fa~\2\u06c5\u06c7\5\u0128\u0095\2\u06c6\u06c5\3\2")
        buf.write("\2\2\u06c6\u06c7\3\2\2\2\u06c7\u00f9\3\2\2\2\u06c8\u06ce")
        buf.write("\5\u00fc\177\2\u06c9\u06ca\5\u00fe\u0080\2\u06ca\u06cb")
        buf.write("\5\u0100\u0081\2\u06cb\u06cc\5\u0102\u0082\2\u06cc\u06ce")
        buf.write("\3\2\2\2\u06cd\u06c8\3\2\2\2\u06cd\u06c9\3\2\2\2\u06ce")
        buf.write("\u00fb\3\2\2\2\u06cf\u06d4\5\u00fe\u0080\2\u06d0\u06d1")
        buf.write("\5\u0104\u0083\2\u06d1\u06d2\5\u00fc\177\2\u06d2\u06d4")
        buf.write("\3\2\2\2\u06d3\u06cf\3\2\2\2\u06d3\u06d0\3\2\2\2\u06d4")
        buf.write("\u00fd\3\2\2\2\u06d5\u06d6\b\u0080\1\2\u06d6\u06d8\5\u010c")
        buf.write("\u0087\2\u06d7\u06d9\5\u00e0q\2\u06d8\u06d7\3\2\2\2\u06d8")
        buf.write("\u06d9\3\2\2\2\u06d9\u06df\3\2\2\2\u06da\u06db\7R\2\2")
        buf.write("\u06db\u06dc\5\u00fc\177\2\u06dc\u06dd\7S\2\2\u06dd\u06df")
        buf.write("\3\2\2\2\u06de\u06d5\3\2\2\2\u06de\u06da\3\2\2\2\u06df")
        buf.write("\u06ed\3\2\2\2\u06e0\u06e1\f\5\2\2\u06e1\u06ec\5\u0100")
        buf.write("\u0081\2\u06e2\u06e3\f\4\2\2\u06e3\u06e5\7T\2\2\u06e4")
        buf.write("\u06e6\5`\61\2\u06e5\u06e4\3\2\2\2\u06e5\u06e6\3\2\2\2")
        buf.write("\u06e6\u06e7\3\2\2\2\u06e7\u06e9\7U\2\2\u06e8\u06ea\5")
        buf.write("\u00e0q\2\u06e9\u06e8\3\2\2\2\u06e9\u06ea\3\2\2\2\u06ea")
        buf.write("\u06ec\3\2\2\2\u06eb\u06e0\3\2\2\2\u06eb\u06e2\3\2\2\2")
        buf.write("\u06ec\u06ef\3\2\2\2\u06ed\u06eb\3\2\2\2\u06ed\u06ee\3")
        buf.write("\2\2\2\u06ee\u00ff\3\2\2\2\u06ef\u06ed\3\2\2\2\u06f0\u06f1")
        buf.write("\7R\2\2\u06f1\u06f2\5\u011a\u008e\2\u06f2\u06f4\7S\2\2")
        buf.write("\u06f3\u06f5\5\u0106\u0084\2\u06f4\u06f3\3\2\2\2\u06f4")
        buf.write("\u06f5\3\2\2\2\u06f5\u06f7\3\2\2\2\u06f6\u06f8\5\u010a")
        buf.write("\u0086\2\u06f7\u06f6\3\2\2\2\u06f7\u06f8\3\2\2\2\u06f8")
        buf.write("\u06fa\3\2\2\2\u06f9\u06fb\5\u018e\u00c8\2\u06fa\u06f9")
        buf.write("\3\2\2\2\u06fa\u06fb\3\2\2\2\u06fb\u06fd\3\2\2\2\u06fc")
        buf.write("\u06fe\5\u00e0q\2\u06fd\u06fc\3\2\2\2\u06fd\u06fe\3\2")
        buf.write("\2\2\u06fe\u0101\3\2\2\2\u06ff\u0700\7y\2\2\u0700\u0702")
        buf.write("\5\u00a6T\2\u0701\u0703\5\u0110\u0089\2\u0702\u0701\3")
        buf.write("\2\2\2\u0702\u0703\3\2\2\2\u0703\u0103\3\2\2\2\u0704\u0706")
        buf.write("\7Z\2\2\u0705\u0707\5\u00e0q\2\u0706\u0705\3\2\2\2\u0706")
        buf.write("\u0707\3\2\2\2\u0707\u0709\3\2\2\2\u0708\u070a\5\u0106")
        buf.write("\u0084\2\u0709\u0708\3\2\2\2\u0709\u070a\3\2\2\2\u070a")
        buf.write("\u071c\3\2\2\2\u070b\u070d\7^\2\2\u070c\u070e\5\u00e0")
        buf.write("q\2\u070d\u070c\3\2\2\2\u070d\u070e\3\2\2\2\u070e\u071c")
        buf.write("\3\2\2\2\u070f\u0711\7s\2\2\u0710\u0712\5\u00e0q\2\u0711")
        buf.write("\u0710\3\2\2\2\u0711\u0712\3\2\2\2\u0712\u071c\3\2\2\2")
        buf.write("\u0713\u0714\5\f\7\2\u0714\u0716\7Z\2\2\u0715\u0717\5")
        buf.write("\u00e0q\2\u0716\u0715\3\2\2\2\u0716\u0717\3\2\2\2\u0717")
        buf.write("\u0719\3\2\2\2\u0718\u071a\5\u0106\u0084\2\u0719\u0718")
        buf.write("\3\2\2\2\u0719\u071a\3\2\2\2\u071a\u071c\3\2\2\2\u071b")
        buf.write("\u0704\3\2\2\2\u071b\u070b\3\2\2\2\u071b\u070f\3\2\2\2")
        buf.write("\u071b\u0713\3\2\2\2\u071c\u0105\3\2\2\2\u071d\u071f\5")
        buf.write("\u0108\u0085\2\u071e\u0720\5\u0106\u0084\2\u071f\u071e")
        buf.write("\3\2\2\2\u071f\u0720\3\2\2\2\u0720\u0107\3\2\2\2\u0721")
        buf.write("\u0722\t\6\2\2\u0722\u0109\3\2\2\2\u0723\u0724\t\7\2\2")
        buf.write("\u0724\u010b\3\2\2\2\u0725\u0727\7\u0080\2\2\u0726\u0725")
        buf.write("\3\2\2\2\u0726\u0727\3\2\2\2\u0727\u0728\3\2\2\2\u0728")
        buf.write("\u0729\5\6\4\2\u0729\u010d\3\2\2\2\u072a\u072c\5\u00a4")
        buf.write("S\2\u072b\u072d\5\u0110\u0089\2\u072c\u072b\3\2\2\2\u072c")
        buf.write("\u072d\3\2\2\2\u072d\u010f\3\2\2\2\u072e\u0737\5\u0112")
        buf.write("\u008a\2\u072f\u0731\5\u0114\u008b\2\u0730\u072f\3\2\2")
        buf.write("\2\u0730\u0731\3\2\2\2\u0731\u0732\3\2\2\2\u0732\u0733")
        buf.write("\5\u0100\u0081\2\u0733\u0734\5\u0102\u0082\2\u0734\u0737")
        buf.write("\3\2\2\2\u0735\u0737\5\u0116\u008c\2\u0736\u072e\3\2\2")
        buf.write("\2\u0736\u0730\3\2\2\2\u0736\u0735\3\2\2\2\u0737\u0111")
        buf.write("\3\2\2\2\u0738\u073e\5\u0114\u008b\2\u0739\u073b\5\u0104")
        buf.write("\u0083\2\u073a\u073c\5\u0112\u008a\2\u073b\u073a\3\2\2")
        buf.write("\2\u073b\u073c\3\2\2\2\u073c\u073e\3\2\2\2\u073d\u0738")
        buf.write("\3\2\2\2\u073d\u0739\3\2\2\2\u073e\u0113\3\2\2\2\u073f")
        buf.write("\u0740\b\u008b\1\2\u0740\u074e\5\u0100\u0081\2\u0741\u0743")
        buf.write("\7T\2\2\u0742\u0744\5`\61\2\u0743\u0742\3\2\2\2\u0743")
        buf.write("\u0744\3\2\2\2\u0744\u0745\3\2\2\2\u0745\u0747\7U\2\2")
        buf.write("\u0746\u0748\5\u00e0q\2\u0747\u0746\3\2\2\2\u0747\u0748")
        buf.write("\3\2\2\2\u0748\u074e\3\2\2\2\u0749\u074a\7R\2\2\u074a")
        buf.write("\u074b\5\u0112\u008a\2\u074b\u074c\7S\2\2\u074c\u074e")
        buf.write("\3\2\2\2\u074d\u073f\3\2\2\2\u074d\u0741\3\2\2\2\u074d")
        buf.write("\u0749\3\2\2\2\u074e\u075c\3\2\2\2\u074f\u0750\f\7\2\2")
        buf.write("\u0750\u075b\5\u0100\u0081\2\u0751\u0752\f\5\2\2\u0752")
        buf.write("\u0754\7T\2\2\u0753\u0755\5`\61\2\u0754\u0753\3\2\2\2")
        buf.write("\u0754\u0755\3\2\2\2\u0755\u0756\3\2\2\2\u0756\u0758\7")
        buf.write("U\2\2\u0757\u0759\5\u00e0q\2\u0758\u0757\3\2\2\2\u0758")
        buf.write("\u0759\3\2\2\2\u0759\u075b\3\2\2\2\u075a\u074f\3\2\2\2")
        buf.write("\u075a\u0751\3\2\2\2\u075b\u075e\3\2\2\2\u075c\u075a\3")
        buf.write("\2\2\2\u075c\u075d\3\2\2\2\u075d\u0115\3\2\2\2\u075e\u075c")
        buf.write("\3\2\2\2\u075f\u0764\5\u0118\u008d\2\u0760\u0761\5\u0104")
        buf.write("\u0083\2\u0761\u0762\5\u0116\u008c\2\u0762\u0764\3\2\2")
        buf.write("\2\u0763\u075f\3\2\2\2\u0763\u0760\3\2\2\2\u0764\u0117")
        buf.write("\3\2\2\2\u0765\u0766\b\u008d\1\2\u0766\u0767\7\u0080\2")
        buf.write("\2\u0767\u0775\3\2\2\2\u0768\u0769\f\5\2\2\u0769\u0774")
        buf.write("\5\u0100\u0081\2\u076a\u076b\f\4\2\2\u076b\u076d\7T\2")
        buf.write("\2\u076c\u076e\5`\61\2\u076d\u076c\3\2\2\2\u076d\u076e")
        buf.write("\3\2\2\2\u076e\u076f\3\2\2\2\u076f\u0771\7U\2\2\u0770")
        buf.write("\u0772\5\u00e0q\2\u0771\u0770\3\2\2\2\u0771\u0772\3\2")
        buf.write("\2\2\u0772\u0774\3\2\2\2\u0773\u0768\3\2\2\2\u0773\u076a")
        buf.write("\3\2\2\2\u0774\u0777\3\2\2\2\u0775\u0773\3\2\2\2\u0775")
        buf.write("\u0776\3\2\2\2\u0776\u0119\3\2\2\2\u0777\u0775\3\2\2\2")
        buf.write("\u0778\u077a\5\u011c\u008f\2\u0779\u0778\3\2\2\2\u0779")
        buf.write("\u077a\3\2\2\2\u077a\u077c\3\2\2\2\u077b\u077d\7\u0080")
        buf.write("\2\2\u077c\u077b\3\2\2\2\u077c\u077d\3\2\2\2\u077d\u0783")
        buf.write("\3\2\2\2\u077e\u077f\5\u011c\u008f\2\u077f\u0780\7w\2")
        buf.write("\2\u0780\u0781\7\u0080\2\2\u0781\u0783\3\2\2\2\u0782\u0779")
        buf.write("\3\2\2\2\u0782\u077e\3\2\2\2\u0783\u011b\3\2\2\2\u0784")
        buf.write("\u0785\b\u008f\1\2\u0785\u0786\5\u011e\u0090\2\u0786\u078c")
        buf.write("\3\2\2\2\u0787\u0788\f\3\2\2\u0788\u0789\7w\2\2\u0789")
        buf.write("\u078b\5\u011e\u0090\2\u078a\u0787\3\2\2\2\u078b\u078e")
        buf.write("\3\2\2\2\u078c\u078a\3\2\2\2\u078c\u078d\3\2\2\2\u078d")
        buf.write("\u011d\3\2\2\2\u078e\u078c\3\2\2\2\u078f\u0791\5\u00e0")
        buf.write("q\2\u0790\u078f\3\2\2\2\u0790\u0791\3\2\2\2\u0791\u0792")
        buf.write("\3\2\2\2\u0792\u0793\5\u0098M\2\u0793\u0794\5\u00fa~\2")
        buf.write("\u0794\u07af\3\2\2\2\u0795\u0797\5\u00e0q\2\u0796\u0795")
        buf.write("\3\2\2\2\u0796\u0797\3\2\2\2\u0797\u0798\3\2\2\2\u0798")
        buf.write("\u0799\5\u0098M\2\u0799\u079a\5\u00fa~\2\u079a\u079b\7")
        buf.write("b\2\2\u079b\u079c\5\u012c\u0097\2\u079c\u07af\3\2\2\2")
        buf.write("\u079d\u079f\5\u00e0q\2\u079e\u079d\3\2\2\2\u079e\u079f")
        buf.write("\3\2\2\2\u079f\u07a0\3\2\2\2\u07a0\u07a2\5\u0098M\2\u07a1")
        buf.write("\u07a3\5\u0110\u0089\2\u07a2\u07a1\3\2\2\2\u07a2\u07a3")
        buf.write("\3\2\2\2\u07a3\u07af\3\2\2\2\u07a4\u07a6\5\u00e0q\2\u07a5")
        buf.write("\u07a4\3\2\2\2\u07a5\u07a6\3\2\2\2\u07a6\u07a7\3\2\2\2")
        buf.write("\u07a7\u07a9\5\u0098M\2\u07a8\u07aa\5\u0110\u0089\2\u07a9")
        buf.write("\u07a8\3\2\2\2\u07a9\u07aa\3\2\2\2\u07aa\u07ab\3\2\2\2")
        buf.write("\u07ab\u07ac\7b\2\2\u07ac\u07ad\5\u012c\u0097\2\u07ad")
        buf.write("\u07af\3\2\2\2\u07ae\u0790\3\2\2\2\u07ae\u0796\3\2\2\2")
        buf.write("\u07ae\u079e\3\2\2\2\u07ae\u07a5\3\2\2\2\u07af\u011f\3")
        buf.write("\2\2\2\u07b0\u07b2\5\u00e0q\2\u07b1\u07b0\3\2\2\2\u07b1")
        buf.write("\u07b2\3\2\2\2\u07b2\u07b4\3\2\2\2\u07b3\u07b5\5\u0098")
        buf.write("M\2\u07b4\u07b3\3\2\2\2\u07b4\u07b5\3\2\2\2\u07b5\u07b6")
        buf.write("\3\2\2\2\u07b6\u07b8\5\u00fa~\2\u07b7\u07b9\5\u0146\u00a4")
        buf.write("\2\u07b8\u07b7\3\2\2\2\u07b8\u07b9\3\2\2\2\u07b9\u07ba")
        buf.write("\3\2\2\2\u07ba\u07bb\5\u0122\u0092\2\u07bb\u0121\3\2\2")
        buf.write("\2\u07bc\u07be\5\u015e\u00b0\2\u07bd\u07bc\3\2\2\2\u07bd")
        buf.write("\u07be\3\2\2\2\u07be\u07bf\3\2\2\2\u07bf\u07c8\5l\67\2")
        buf.write("\u07c0\u07c8\5\u0184\u00c3\2\u07c1\u07c2\7b\2\2\u07c2")
        buf.write("\u07c3\7\30\2\2\u07c3\u07c8\7}\2\2\u07c4\u07c5\7b\2\2")
        buf.write("\u07c5\u07c6\7\31\2\2\u07c6\u07c8\7}\2\2\u07c7\u07bd\3")
        buf.write("\2\2\2\u07c7\u07c0\3\2\2\2\u07c7\u07c1\3\2\2\2\u07c7\u07c4")
        buf.write("\3\2\2\2\u07c8\u0123\3\2\2\2\u07c9\u07cb\5\u00e0q\2\u07ca")
        buf.write("\u07c9\3\2\2\2\u07ca\u07cb\3\2\2\2\u07cb\u07cd\3\2\2\2")
        buf.write("\u07cc\u07ce\5\u0098M\2\u07cd\u07cc\3\2\2\2\u07cd\u07ce")
        buf.write("\3\2\2\2\u07ce\u07cf\3\2\2\2\u07cf\u07d1\5\u00fa~\2\u07d0")
        buf.write("\u07d2\5\u0146\u00a4\2\u07d1\u07d0\3\2\2\2\u07d1\u07d2")
        buf.write("\3\2\2\2\u07d2\u07d3\3\2\2\2\u07d3\u07d4\5\u0126\u0094")
        buf.write("\2\u07d4\u0125\3\2\2\2\u07d5\u07d6\5n8\2\u07d6\u0127\3")
        buf.write("\2\2\2\u07d7\u07dd\5\u012a\u0096\2\u07d8\u07d9\7R\2\2")
        buf.write("\u07d9\u07da\5\"\22\2\u07da\u07db\7S\2\2\u07db\u07dd\3")
        buf.write("\2\2\2\u07dc\u07d7\3\2\2\2\u07dc\u07d8\3\2\2\2\u07dd\u0129")
        buf.write("\3\2\2\2\u07de\u07df\7b\2\2\u07df\u07e2\5\u012c\u0097")
        buf.write("\2\u07e0\u07e2\5\u0130\u0099\2\u07e1\u07de\3\2\2\2\u07e1")
        buf.write("\u07e0\3\2\2\2\u07e2\u012b\3\2\2\2\u07e3\u07e6\5T+\2\u07e4")
        buf.write("\u07e6\5\u0130\u0099\2\u07e5\u07e3\3\2\2\2\u07e5\u07e4")
        buf.write("\3\2\2\2\u07e6\u012d\3\2\2\2\u07e7\u07e8\b\u0098\1\2\u07e8")
        buf.write("\u07ea\5\u012c\u0097\2\u07e9\u07eb\7\u0080\2\2\u07ea\u07e9")
        buf.write("\3\2\2\2\u07ea\u07eb\3\2\2\2\u07eb\u07f4\3\2\2\2\u07ec")
        buf.write("\u07ed\f\3\2\2\u07ed\u07ee\7w\2\2\u07ee\u07f0\5\u012c")
        buf.write("\u0097\2\u07ef\u07f1\7\u0080\2\2\u07f0\u07ef\3\2\2\2\u07f0")
        buf.write("\u07f1\3\2\2\2\u07f1\u07f3\3\2\2\2\u07f2\u07ec\3\2\2\2")
        buf.write("\u07f3\u07f6\3\2\2\2\u07f4\u07f2\3\2\2\2\u07f4\u07f5\3")
        buf.write("\2\2\2\u07f5\u012f\3\2\2\2\u07f6\u07f4\3\2\2\2\u07f7\u07f8")
        buf.write("\7V\2\2\u07f8\u07fa\5\u012e\u0098\2\u07f9\u07fb\7w\2\2")
        buf.write("\u07fa\u07f9\3\2\2\2\u07fa\u07fb\3\2\2\2\u07fb\u07fc\3")
        buf.write("\2\2\2\u07fc\u07fd\7W\2\2\u07fd\u0801\3\2\2\2\u07fe\u07ff")
        buf.write("\7V\2\2\u07ff\u0801\7W\2\2\u0800\u07f7\3\2\2\2\u0800\u07fe")
        buf.write("\3\2\2\2\u0801\u0131\3\2\2\2\u0802\u0805\7\u0081\2\2\u0803")
        buf.write("\u0805\5\u0172\u00ba\2\u0804\u0802\3\2\2\2\u0804\u0803")
        buf.write("\3\2\2\2\u0805\u0133\3\2\2\2\u0806\u0807\5\u0136\u009c")
        buf.write("\2\u0807\u0809\7V\2\2\u0808\u080a\5\u013e\u00a0\2\u0809")
        buf.write("\u0808\3\2\2\2\u0809\u080a\3\2\2\2\u080a\u080b\3\2\2\2")
        buf.write("\u080b\u080c\7W\2\2\u080c\u0135\3\2\2\2\u080d\u080f\5")
        buf.write("\u013c\u009f\2\u080e\u0810\5\u00e0q\2\u080f\u080e\3\2")
        buf.write("\2\2\u080f\u0810\3\2\2\2\u0810\u0811\3\2\2\2\u0811\u0813")
        buf.write("\5\u0138\u009d\2\u0812\u0814\5\u013a\u009e\2\u0813\u0812")
        buf.write("\3\2\2\2\u0813\u0814\3\2\2\2\u0814\u0816\3\2\2\2\u0815")
        buf.write("\u0817\5\u014c\u00a7\2\u0816\u0815\3\2\2\2\u0816\u0817")
        buf.write("\3\2\2\2\u0817\u0820\3\2\2\2\u0818\u081a\5\u013c\u009f")
        buf.write("\2\u0819\u081b\5\u00e0q\2\u081a\u0819\3\2\2\2\u081a\u081b")
        buf.write("\3\2\2\2\u081b\u081d\3\2\2\2\u081c\u081e\5\u014c\u00a7")
        buf.write("\2\u081d\u081c\3\2\2\2\u081d\u081e\3\2\2\2\u081e\u0820")
        buf.write("\3\2\2\2\u081f\u080d\3\2\2\2\u081f\u0818\3\2\2\2\u0820")
        buf.write("\u0137\3\2\2\2\u0821\u0823\5\f\7\2\u0822\u0821\3\2\2\2")
        buf.write("\u0822\u0823\3\2\2\2\u0823\u0824\3\2\2\2\u0824\u0825\5")
        buf.write("\u0132\u009a\2\u0825\u0139\3\2\2\2\u0826\u0827\7#\2\2")
        buf.write("\u0827\u013b\3\2\2\2\u0828\u0829\t\b\2\2\u0829\u013d\3")
        buf.write("\2\2\2\u082a\u082c\5\u0140\u00a1\2\u082b\u082d\5\u013e")
        buf.write("\u00a0\2\u082c\u082b\3\2\2\2\u082c\u082d\3\2\2\2\u082d")
        buf.write("\u0834\3\2\2\2\u082e\u082f\5\u0156\u00ac\2\u082f\u0831")
        buf.write("\7{\2\2\u0830\u0832\5\u013e\u00a0\2\u0831\u0830\3\2\2")
        buf.write("\2\u0831\u0832\3\2\2\2\u0832\u0834\3\2\2\2\u0833\u082a")
        buf.write("\3\2\2\2\u0833\u082e\3\2\2\2\u0834\u013f\3\2\2\2\u0835")
        buf.write("\u0837\5\u00e0q\2\u0836\u0835\3\2\2\2\u0836\u0837\3\2")
        buf.write("\2\2\u0837\u0839\3\2\2\2\u0838\u083a\5\u0098M\2\u0839")
        buf.write("\u0838\3\2\2\2\u0839\u083a\3\2\2\2\u083a\u083c\3\2\2\2")
        buf.write("\u083b\u083d\5\u0142\u00a2\2\u083c\u083b\3\2\2\2\u083c")
        buf.write("\u083d\3\2\2\2\u083d\u083e\3\2\2\2\u083e\u0846\7}\2\2")
        buf.write("\u083f\u0846\5\u0120\u0091\2\u0840\u0846\5\u00d8m\2\u0841")
        buf.write("\u0846\5\u0090I\2\u0842\u0846\5\u016a\u00b6\2\u0843\u0846")
        buf.write("\5\u008cG\2\u0844\u0846\5\u0092J\2\u0845\u0836\3\2\2\2")
        buf.write("\u0845\u083f\3\2\2\2\u0845\u0840\3\2\2\2\u0845\u0841\3")
        buf.write("\2\2\2\u0845\u0842\3\2\2\2\u0845\u0843\3\2\2\2\u0845\u0844")
        buf.write("\3\2\2\2\u0846\u0141\3\2\2\2\u0847\u0848\b\u00a2\1\2\u0848")
        buf.write("\u0849\5\u0144\u00a3\2\u0849\u084f\3\2\2\2\u084a\u084b")
        buf.write("\f\3\2\2\u084b\u084c\7w\2\2\u084c\u084e\5\u0144\u00a3")
        buf.write("\2\u084d\u084a\3\2\2\2\u084e\u0851\3\2\2\2\u084f\u084d")
        buf.write("\3\2\2\2\u084f\u0850\3\2\2\2\u0850\u0143\3\2\2\2\u0851")
        buf.write("\u084f\3\2\2\2\u0852\u0854\5\u00fa~\2\u0853\u0855\5\u0146")
        buf.write("\u00a4\2\u0854\u0853\3\2\2\2\u0854\u0855\3\2\2\2\u0855")
        buf.write("\u0857\3\2\2\2\u0856\u0858\5\u014a\u00a6\2\u0857\u0856")
        buf.write("\3\2\2\2\u0857\u0858\3\2\2\2\u0858\u0866\3\2\2\2\u0859")
        buf.write("\u085b\5\u00fa~\2\u085a\u085c\5\u012a\u0096\2\u085b\u085a")
        buf.write("\3\2\2\2\u085b\u085c\3\2\2\2\u085c\u0866\3\2\2\2\u085d")
        buf.write("\u085f\7\u0081\2\2\u085e\u085d\3\2\2\2\u085e\u085f\3\2")
        buf.write("\2\2\u085f\u0861\3\2\2\2\u0860\u0862\5\u00e0q\2\u0861")
        buf.write("\u0860\3\2\2\2\u0861\u0862\3\2\2\2\u0862\u0863\3\2\2\2")
        buf.write("\u0863\u0864\7{\2\2\u0864\u0866\5`\61\2\u0865\u0852\3")
        buf.write("\2\2\2\u0865\u0859\3\2\2\2\u0865\u085e\3\2\2\2\u0866\u0145")
        buf.write("\3\2\2\2\u0867\u0868\b\u00a4\1\2\u0868\u0869\5\u0148\u00a5")
        buf.write("\2\u0869\u086e\3\2\2\2\u086a\u086b\f\3\2\2\u086b\u086d")
        buf.write("\5\u0148\u00a5\2\u086c\u086a\3\2\2\2\u086d\u0870\3\2\2")
        buf.write("\2\u086e\u086c\3\2\2\2\u086e\u086f\3\2\2\2\u086f\u0147")
        buf.write("\3\2\2\2\u0870\u086e\3\2\2\2\u0871\u0872\t\t\2\2\u0872")
        buf.write("\u0149\3\2\2\2\u0873\u0874\7b\2\2\u0874\u0875\7\u0084")
        buf.write("\2\2\u0875\u0876\b\u00a6\1\2\u0876\u014b\3\2\2\2\u0877")
        buf.write("\u0878\7{\2\2\u0878\u0879\5\u014e\u00a8\2\u0879\u014d")
        buf.write("\3\2\2\2\u087a\u087b\b\u00a8\1\2\u087b\u087d\5\u0150\u00a9")
        buf.write("\2\u087c\u087e\7\u0080\2\2\u087d\u087c\3\2\2\2\u087d\u087e")
        buf.write("\3\2\2\2\u087e\u0887\3\2\2\2\u087f\u0880\f\3\2\2\u0880")
        buf.write("\u0881\7w\2\2\u0881\u0883\5\u0150\u00a9\2\u0882\u0884")
        buf.write("\7\u0080\2\2\u0883\u0882\3\2\2\2\u0883\u0884\3\2\2\2\u0884")
        buf.write("\u0886\3\2\2\2\u0885\u087f\3\2\2\2\u0886\u0889\3\2\2\2")
        buf.write("\u0887\u0885\3\2\2\2\u0887\u0888\3\2\2\2\u0888\u014f\3")
        buf.write("\2\2\2\u0889\u0887\3\2\2\2\u088a\u088c\5\u00e0q\2\u088b")
        buf.write("\u088a\3\2\2\2\u088b\u088c\3\2\2\2\u088c\u088d\3\2\2\2")
        buf.write("\u088d\u08a0\5\u0154\u00ab\2\u088e\u0890\5\u00e0q\2\u088f")
        buf.write("\u088e\3\2\2\2\u088f\u0890\3\2\2\2\u0890\u0891\3\2\2\2")
        buf.write("\u0891\u0893\7M\2\2\u0892\u0894\5\u0156\u00ac\2\u0893")
        buf.write("\u0892\3\2\2\2\u0893\u0894\3\2\2\2\u0894\u0895\3\2\2\2")
        buf.write("\u0895\u08a0\5\u0154\u00ab\2\u0896\u0898\5\u00e0q\2\u0897")
        buf.write("\u0896\3\2\2\2\u0897\u0898\3\2\2\2\u0898\u0899\3\2\2\2")
        buf.write("\u0899\u089b\5\u0156\u00ac\2\u089a\u089c\7M\2\2\u089b")
        buf.write("\u089a\3\2\2\2\u089b\u089c\3\2\2\2\u089c\u089d\3\2\2\2")
        buf.write("\u089d\u089e\5\u0154\u00ab\2\u089e\u08a0\3\2\2\2\u089f")
        buf.write("\u088b\3\2\2\2\u089f\u088f\3\2\2\2\u089f\u0897\3\2\2\2")
        buf.write("\u08a0\u0151\3\2\2\2\u08a1\u08a3\5\f\7\2\u08a2\u08a1\3")
        buf.write("\2\2\2\u08a2\u08a3\3\2\2\2\u08a3\u08a4\3\2\2\2\u08a4\u08a7")
        buf.write("\5\u0132\u009a\2\u08a5\u08a7\5\u00acW\2\u08a6\u08a2\3")
        buf.write("\2\2\2\u08a6\u08a5\3\2\2\2\u08a7\u0153\3\2\2\2\u08a8\u08a9")
        buf.write("\5\u0152\u00aa\2\u08a9\u0155\3\2\2\2\u08aa\u08ab\t\n\2")
        buf.write("\2\u08ab\u0157\3\2\2\2\u08ac\u08ad\7\61\2\2\u08ad\u08ae")
        buf.write("\5\u015a\u00ae\2\u08ae\u0159\3\2\2\2\u08af\u08b1\5\u00a4")
        buf.write("S\2\u08b0\u08b2\5\u015c\u00af\2\u08b1\u08b0\3\2\2\2\u08b1")
        buf.write("\u08b2\3\2\2\2\u08b2\u015b\3\2\2\2\u08b3\u08b5\5\u0104")
        buf.write("\u0083\2\u08b4\u08b6\5\u015c\u00af\2\u08b5\u08b4\3\2\2")
        buf.write("\2\u08b5\u08b6\3\2\2\2\u08b6\u015d\3\2\2\2\u08b7\u08b8")
        buf.write("\7{\2\2\u08b8\u08b9\5\u0160\u00b1\2\u08b9\u015f\3\2\2")
        buf.write("\2\u08ba\u08bc\5\u0162\u00b2\2\u08bb\u08bd\7\u0080\2\2")
        buf.write("\u08bc\u08bb\3\2\2\2\u08bc\u08bd\3\2\2\2\u08bd\u08c6\3")
        buf.write("\2\2\2\u08be\u08c0\5\u0162\u00b2\2\u08bf\u08c1\7\u0080")
        buf.write("\2\2\u08c0\u08bf\3\2\2\2\u08c0\u08c1\3\2\2\2\u08c1\u08c2")
        buf.write("\3\2\2\2\u08c2\u08c3\7w\2\2\u08c3\u08c4\5\u0160\u00b1")
        buf.write("\2\u08c4\u08c6\3\2\2\2\u08c5\u08ba\3\2\2\2\u08c5\u08be")
        buf.write("\3\2\2\2\u08c6\u0161\3\2\2\2\u08c7\u08c8\5\u0164\u00b3")
        buf.write("\2\u08c8\u08ca\7R\2\2\u08c9\u08cb\5\"\22\2\u08ca\u08c9")
        buf.write("\3\2\2\2\u08ca\u08cb\3\2\2\2\u08cb\u08cc\3\2\2\2\u08cc")
        buf.write("\u08cd\7S\2\2\u08cd\u08d2\3\2\2\2\u08ce\u08cf\5\u0164")
        buf.write("\u00b3\2\u08cf\u08d0\5\u0130\u0099\2\u08d0\u08d2\3\2\2")
        buf.write("\2\u08d1\u08c7\3\2\2\2\u08d1\u08ce\3\2\2\2\u08d2\u0163")
        buf.write("\3\2\2\2\u08d3\u08d6\5\u0152\u00aa\2\u08d4\u08d6\7\u0081")
        buf.write("\2\2\u08d5\u08d3\3\2\2\2\u08d5\u08d4\3\2\2\2\u08d6\u0165")
        buf.write("\3\2\2\2\u08d7\u08d8\7\61\2\2\u08d8\u08d9\5\u019a\u00ce")
        buf.write("\2\u08d9\u0167\3\2\2\2\u08da\u08db\7\61\2\2\u08db\u08dc")
        buf.write("\7\u008a\2\2\u08dc\u08e0\7\u0081\2\2\u08dd\u08de\7\61")
        buf.write("\2\2\u08de\u08e0\7\u008d\2\2\u08df\u08da\3\2\2\2\u08df")
        buf.write("\u08dd\3\2\2\2\u08e0\u0169\3\2\2\2\u08e1\u08e2\7A\2\2")
        buf.write("\u08e2\u08e3\7c\2\2\u08e3\u08e4\5\u016c\u00b7\2\u08e4")
        buf.write("\u08e5\7d\2\2\u08e5\u08e6\5\u0088E\2\u08e6\u016b\3\2\2")
        buf.write("\2\u08e7\u08e8\b\u00b7\1\2\u08e8\u08e9\5\u016e\u00b8\2")
        buf.write("\u08e9\u08ef\3\2\2\2\u08ea\u08eb\f\3\2\2\u08eb\u08ec\7")
        buf.write("w\2\2\u08ec\u08ee\5\u016e\u00b8\2\u08ed\u08ea\3\2\2\2")
        buf.write("\u08ee\u08f1\3\2\2\2\u08ef\u08ed\3\2\2\2\u08ef\u08f0\3")
        buf.write("\2\2\2\u08f0\u016d\3\2\2\2\u08f1\u08ef\3\2\2\2\u08f2\u08f5")
        buf.write("\5\u0170\u00b9\2\u08f3\u08f5\5\u011e\u0090\2\u08f4\u08f2")
        buf.write("\3\2\2\2\u08f4\u08f3\3\2\2\2\u08f5\u016f\3\2\2\2\u08f6")
        buf.write("\u08f8\7\20\2\2\u08f7\u08f9\7\u0080\2\2\u08f8\u08f7\3")
        buf.write("\2\2\2\u08f8\u08f9\3\2\2\2\u08f9\u08fb\3\2\2\2\u08fa\u08fc")
        buf.write("\7\u0081\2\2\u08fb\u08fa\3\2\2\2\u08fb\u08fc\3\2\2\2\u08fc")
        buf.write("\u0927\3\2\2\2\u08fd\u08ff\7\20\2\2\u08fe\u0900\7\u0081")
        buf.write("\2\2\u08ff\u08fe\3\2\2\2\u08ff\u0900\3\2\2\2\u0900\u0901")
        buf.write("\3\2\2\2\u0901\u0902\7b\2\2\u0902\u0927\5\u010e\u0088")
        buf.write("\2\u0903\u0905\7I\2\2\u0904\u0906\7\u0080\2\2\u0905\u0904")
        buf.write("\3\2\2\2\u0905\u0906\3\2\2\2\u0906\u0908\3\2\2\2\u0907")
        buf.write("\u0909\7\u0081\2\2\u0908\u0907\3\2\2\2\u0908\u0909\3\2")
        buf.write("\2\2\u0909\u0927\3\2\2\2\u090a\u090c\7I\2\2\u090b\u090d")
        buf.write("\7\u0081\2\2\u090c\u090b\3\2\2\2\u090c\u090d\3\2\2\2\u090d")
        buf.write("\u090e\3\2\2\2\u090e\u090f\7b\2\2\u090f\u0927\5\u010e")
        buf.write("\u0088\2\u0910\u0911\7A\2\2\u0911\u0912\7c\2\2\u0912\u0913")
        buf.write("\5\u016c\u00b7\2\u0913\u0914\7d\2\2\u0914\u0916\7\20\2")
        buf.write("\2\u0915\u0917\7\u0080\2\2\u0916\u0915\3\2\2\2\u0916\u0917")
        buf.write("\3\2\2\2\u0917\u0919\3\2\2\2\u0918\u091a\7\u0081\2\2\u0919")
        buf.write("\u0918\3\2\2\2\u0919\u091a\3\2\2\2\u091a\u0927\3\2\2\2")
        buf.write("\u091b\u091c\7A\2\2\u091c\u091d\7c\2\2\u091d\u091e\5\u016c")
        buf.write("\u00b7\2\u091e\u091f\7d\2\2\u091f\u0921\7\20\2\2\u0920")
        buf.write("\u0922\7\u0081\2\2\u0921\u0920\3\2\2\2\u0921\u0922\3\2")
        buf.write("\2\2\u0922\u0923\3\2\2\2\u0923\u0924\7b\2\2\u0924\u0925")
        buf.write("\5\6\4\2\u0925\u0927\3\2\2\2\u0926\u08f6\3\2\2\2\u0926")
        buf.write("\u08fd\3\2\2\2\u0926\u0903\3\2\2\2\u0926\u090a\3\2\2\2")
        buf.write("\u0926\u0910\3\2\2\2\u0926\u091b\3\2\2\2\u0927\u0171\3")
        buf.write("\2\2\2\u0928\u0929\5\u0176\u00bc\2\u0929\u092b\7c\2\2")
        buf.write("\u092a\u092c\5\u0178\u00bd\2\u092b\u092a\3\2\2\2\u092b")
        buf.write("\u092c\3\2\2\2\u092c\u092d\3\2\2\2\u092d\u092e\7d\2\2")
        buf.write("\u092e\u0173\3\2\2\2\u092f\u093f\5\u0172\u00ba\2\u0930")
        buf.write("\u0931\5\u0166\u00b4\2\u0931\u0933\7c\2\2\u0932\u0934")
        buf.write("\5\u0178\u00bd\2\u0933\u0932\3\2\2\2\u0933\u0934\3\2\2")
        buf.write("\2\u0934\u0935\3\2\2\2\u0935\u0936\7d\2\2\u0936\u093f")
        buf.write("\3\2\2\2\u0937\u0938\5\u0168\u00b5\2\u0938\u093a\7c\2")
        buf.write("\2\u0939\u093b\5\u0178\u00bd\2\u093a\u0939\3\2\2\2\u093a")
        buf.write("\u093b\3\2\2\2\u093b\u093c\3\2\2\2\u093c\u093d\7d\2\2")
        buf.write("\u093d\u093f\3\2\2\2\u093e\u092f\3\2\2\2\u093e\u0930\3")
        buf.write("\2\2\2\u093e\u0937\3\2\2\2\u093f\u0175\3\2\2\2\u0940\u0941")
        buf.write("\7\u0081\2\2\u0941\u0177\3\2\2\2\u0942\u0943\b\u00bd\1")
        buf.write("\2\u0943\u0945\5\u017a\u00be\2\u0944\u0946\7\u0080\2\2")
        buf.write("\u0945\u0944\3\2\2\2\u0945\u0946\3\2\2\2\u0946\u094f\3")
        buf.write("\2\2\2\u0947\u0948\f\3\2\2\u0948\u0949\7w\2\2\u0949\u094b")
        buf.write("\5\u017a\u00be\2\u094a\u094c\7\u0080\2\2\u094b\u094a\3")
        buf.write("\2\2\2\u094b\u094c\3\2\2\2\u094c\u094e\3\2\2\2\u094d\u0947")
        buf.write("\3\2\2\2\u094e\u0951\3\2\2\2\u094f\u094d\3\2\2\2\u094f")
        buf.write("\u0950\3\2\2\2\u0950\u0179\3\2\2\2\u0951\u094f\3\2\2\2")
        buf.write("\u0952\u0956\5\u010e\u0088\2\u0953\u0956\5`\61\2\u0954")
        buf.write("\u0956\5\6\4\2\u0955\u0952\3\2\2\2\u0955\u0953\3\2\2\2")
        buf.write("\u0955\u0954\3\2\2\2\u0956\u017b\3\2\2\2\u0957\u0958\7")
        buf.write("I\2\2\u0958\u0959\5\f\7\2\u0959\u095a\7\u0081\2\2\u095a")
        buf.write("\u0963\3\2\2\2\u095b\u095c\7I\2\2\u095c\u095e\5\f\7\2")
        buf.write("\u095d\u095f\7A\2\2\u095e\u095d\3\2\2\2\u095e\u095f\3")
        buf.write("\2\2\2\u095f\u0960\3\2\2\2\u0960\u0961\5\u0172\u00ba\2")
        buf.write("\u0961\u0963\3\2\2\2\u0962\u0957\3\2\2\2\u0962\u095b\3")
        buf.write("\2\2\2\u0963\u017d\3\2\2\2\u0964\u0966\7!\2\2\u0965\u0964")
        buf.write("\3\2\2\2\u0965\u0966\3\2\2\2\u0966\u0967\3\2\2\2\u0967")
        buf.write("\u0968\7A\2\2\u0968\u0969\5\u0088E\2\u0969\u017f\3\2\2")
        buf.write("\2\u096a\u096b\7A\2\2\u096b\u096c\7c\2\2\u096c\u096d\7")
        buf.write("d\2\2\u096d\u096e\5\u0088E\2\u096e\u0181\3\2\2\2\u096f")
        buf.write("\u0970\7F\2\2\u0970\u0971\5l\67\2\u0971\u0972\5\u0186")
        buf.write("\u00c4\2\u0972\u0183\3\2\2\2\u0973\u0975\7F\2\2\u0974")
        buf.write("\u0976\5\u015e\u00b0\2\u0975\u0974\3\2\2\2\u0975\u0976")
        buf.write("\3\2\2\2\u0976\u0977\3\2\2\2\u0977\u0978\5l\67\2\u0978")
        buf.write("\u0979\5\u0186\u00c4\2\u0979\u0185\3\2\2\2\u097a\u097c")
        buf.write("\5\u0188\u00c5\2\u097b\u097d\5\u0186\u00c4\2\u097c\u097b")
        buf.write("\3\2\2\2\u097c\u097d\3\2\2\2\u097d\u0187\3\2\2\2\u097e")
        buf.write("\u097f\7\f\2\2\u097f\u0980\7R\2\2\u0980\u0981\5\u018a")
        buf.write("\u00c6\2\u0981\u0982\7S\2\2\u0982\u0983\5l\67\2\u0983")
        buf.write("\u0189\3\2\2\2\u0984\u0986\5\u00e0q\2\u0985\u0984\3\2")
        buf.write("\2\2\u0985\u0986\3\2\2\2\u0986\u0987\3\2\2\2\u0987\u0988")
        buf.write("\5\u00a4S\2\u0988\u0989\5\u00fa~\2\u0989\u0993\3\2\2\2")
        buf.write("\u098a\u098c\5\u00e0q\2\u098b\u098a\3\2\2\2\u098b\u098c")
        buf.write("\3\2\2\2\u098c\u098d\3\2\2\2\u098d\u098f\5\u00a4S\2\u098e")
        buf.write("\u0990\5\u0110\u0089\2\u098f\u098e\3\2\2\2\u098f\u0990")
        buf.write("\3\2\2\2\u0990\u0993\3\2\2\2\u0991\u0993\7\u0080\2\2\u0992")
        buf.write("\u0985\3\2\2\2\u0992\u098b\3\2\2\2\u0992\u0991\3\2\2\2")
        buf.write("\u0993\u018b\3\2\2\2\u0994\u0996\7D\2\2\u0995\u0997\5")
        buf.write("T+\2\u0996\u0995\3\2\2\2\u0996\u0997\3\2\2\2\u0997\u018d")
        buf.write("\3\2\2\2\u0998\u099b\5\u0190\u00c9\2\u0999\u099b\5\u0194")
        buf.write("\u00cb\2\u099a\u0998\3\2\2\2\u099a\u0999\3\2\2\2\u099b")
        buf.write("\u018f\3\2\2\2\u099c\u099d\7D\2\2\u099d\u099f\7R\2\2\u099e")
        buf.write("\u09a0\5\u0192\u00ca\2\u099f\u099e\3\2\2\2\u099f\u09a0")
        buf.write("\3\2\2\2\u09a0\u09a1\3\2\2\2\u09a1\u09a2\7S\2\2\u09a2")
        buf.write("\u0191\3\2\2\2\u09a3\u09a4\b\u00ca\1\2\u09a4\u09a6\5\u010e")
        buf.write("\u0088\2\u09a5\u09a7\7\u0080\2\2\u09a6\u09a5\3\2\2\2\u09a6")
        buf.write("\u09a7\3\2\2\2\u09a7\u09b0\3\2\2\2\u09a8\u09a9\f\3\2\2")
        buf.write("\u09a9\u09aa\7w\2\2\u09aa\u09ac\5\u010e\u0088\2\u09ab")
        buf.write("\u09ad\7\u0080\2\2\u09ac\u09ab\3\2\2\2\u09ac\u09ad\3\2")
        buf.write("\2\2\u09ad\u09af\3\2\2\2\u09ae\u09a8\3\2\2\2\u09af\u09b2")
        buf.write("\3\2\2\2\u09b0\u09ae\3\2\2\2\u09b0\u09b1\3\2\2\2\u09b1")
        buf.write("\u0193\3\2\2\2\u09b2\u09b0\3\2\2\2\u09b3\u09b4\7/\2\2")
        buf.write("\u09b4\u09b5\7R\2\2\u09b5\u09b6\5`\61\2\u09b6\u09b7\7")
        buf.write("S\2\2\u09b7\u09ba\3\2\2\2\u09b8\u09ba\7/\2\2\u09b9\u09b3")
        buf.write("\3\2\2\2\u09b9\u09b8\3\2\2\2\u09ba\u0195\3\2\2\2\u09bb")
        buf.write("\u09bc\7d\2\2\u09bc\u09bd\7d\2\2\u09bd\u0197\3\2\2\2\u09be")
        buf.write("\u09bf\7d\2\2\u09bf\u09c0\7d\2\2\u09c0\u09c1\7b\2\2\u09c1")
        buf.write("\u0199\3\2\2\2\u09c2\u09f3\7.\2\2\u09c3\u09f3\7\31\2\2")
        buf.write("\u09c4\u09c5\7.\2\2\u09c5\u09c6\7T\2\2\u09c6\u09f3\7U")
        buf.write("\2\2\u09c7\u09c8\7\31\2\2\u09c8\u09c9\7T\2\2\u09c9\u09f3")
        buf.write("\7U\2\2\u09ca\u09f3\7X\2\2\u09cb\u09f3\7Y\2\2\u09cc\u09f3")
        buf.write("\7Z\2\2\u09cd\u09f3\7[\2\2\u09ce\u09f3\7\\\2\2\u09cf\u09f3")
        buf.write("\7]\2\2\u09d0\u09f3\7^\2\2\u09d1\u09f3\7_\2\2\u09d2\u09f3")
        buf.write("\7`\2\2\u09d3\u09f3\7a\2\2\u09d4\u09f3\7b\2\2\u09d5\u09f3")
        buf.write("\7c\2\2\u09d6\u09f3\7d\2\2\u09d7\u09f3\7e\2\2\u09d8\u09f3")
        buf.write("\7f\2\2\u09d9\u09f3\7g\2\2\u09da\u09f3\7h\2\2\u09db\u09f3")
        buf.write("\7i\2\2\u09dc\u09f3\7j\2\2\u09dd\u09f3\7k\2\2\u09de\u09f3")
        buf.write("\7l\2\2\u09df\u09f3\7m\2\2\u09e0\u09f3\5\u0196\u00cc\2")
        buf.write("\u09e1\u09f3\5\u0198\u00cd\2\u09e2\u09f3\7n\2\2\u09e3")
        buf.write("\u09f3\7o\2\2\u09e4\u09f3\7p\2\2\u09e5\u09f3\7q\2\2\u09e6")
        buf.write("\u09f3\7r\2\2\u09e7\u09f3\7s\2\2\u09e8\u09f3\7t\2\2\u09e9")
        buf.write("\u09f3\7u\2\2\u09ea\u09f3\7v\2\2\u09eb\u09f3\7w\2\2\u09ec")
        buf.write("\u09f3\7x\2\2\u09ed\u09f3\7y\2\2\u09ee\u09ef\7R\2\2\u09ef")
        buf.write("\u09f3\7S\2\2\u09f0\u09f1\7T\2\2\u09f1\u09f3\7U\2\2\u09f2")
        buf.write("\u09c2\3\2\2\2\u09f2\u09c3\3\2\2\2\u09f2\u09c4\3\2\2\2")
        buf.write("\u09f2\u09c7\3\2\2\2\u09f2\u09ca\3\2\2\2\u09f2\u09cb\3")
        buf.write("\2\2\2\u09f2\u09cc\3\2\2\2\u09f2\u09cd\3\2\2\2\u09f2\u09ce")
        buf.write("\3\2\2\2\u09f2\u09cf\3\2\2\2\u09f2\u09d0\3\2\2\2\u09f2")
        buf.write("\u09d1\3\2\2\2\u09f2\u09d2\3\2\2\2\u09f2\u09d3\3\2\2\2")
        buf.write("\u09f2\u09d4\3\2\2\2\u09f2\u09d5\3\2\2\2\u09f2\u09d6\3")
        buf.write("\2\2\2\u09f2\u09d7\3\2\2\2\u09f2\u09d8\3\2\2\2\u09f2\u09d9")
        buf.write("\3\2\2\2\u09f2\u09da\3\2\2\2\u09f2\u09db\3\2\2\2\u09f2")
        buf.write("\u09dc\3\2\2\2\u09f2\u09dd\3\2\2\2\u09f2\u09de\3\2\2\2")
        buf.write("\u09f2\u09df\3\2\2\2\u09f2\u09e0\3\2\2\2\u09f2\u09e1\3")
        buf.write("\2\2\2\u09f2\u09e2\3\2\2\2\u09f2\u09e3\3\2\2\2\u09f2\u09e4")
        buf.write("\3\2\2\2\u09f2\u09e5\3\2\2\2\u09f2\u09e6\3\2\2\2\u09f2")
        buf.write("\u09e7\3\2\2\2\u09f2\u09e8\3\2\2\2\u09f2\u09e9\3\2\2\2")
        buf.write("\u09f2\u09ea\3\2\2\2\u09f2\u09eb\3\2\2\2\u09f2\u09ec\3")
        buf.write("\2\2\2\u09f2\u09ed\3\2\2\2\u09f2\u09ee\3\2\2\2\u09f2\u09f0")
        buf.write("\3\2\2\2\u09f3\u019b\3\2\2\2\u09f4\u09fc\7\u0082\2\2\u09f5")
        buf.write("\u09fc\7\u0088\2\2\u09f6\u09fc\7\u0089\2\2\u09f7\u09fc")
        buf.write("\7\u008a\2\2\u09f8\u09fc\5\u019e\u00d0\2\u09f9\u09fc\5")
        buf.write("\u01a0\u00d1\2\u09fa\u09fc\5\u01a2\u00d2\2\u09fb\u09f4")
        buf.write("\3\2\2\2\u09fb\u09f5\3\2\2\2\u09fb\u09f6\3\2\2\2\u09fb")
        buf.write("\u09f7\3\2\2\2\u09fb\u09f8\3\2\2\2\u09fb\u09f9\3\2\2\2")
        buf.write("\u09fb\u09fa\3\2\2\2\u09fc\u019d\3\2\2\2\u09fd\u09fe\t")
        buf.write("\13\2\2\u09fe\u019f\3\2\2\2\u09ff\u0a00\7\60\2\2\u0a00")
        buf.write("\u01a1\3\2\2\2\u0a01\u0a02\t\f\2\2\u0a02\u01a3\3\2\2\2")
        buf.write("\u0149\u01a5\u01b1\u01b5\u01c0\u01c4\u01d3\u01da\u01df")
        buf.write("\u01e1\u01e6\u01ec\u01f6\u01fd\u0203\u0207\u020c\u0212")
        buf.write("\u0219\u021f\u0222\u0225\u0228\u022f\u0236\u026a\u0279")
        buf.write("\u027f\u0285\u0292\u0294\u029a\u02a9\u02af\u02cd\u02d2")
        buf.write("\u02d6\u02da\u02dd\u02e1\u02e7\u02e9\u02f1\u02f5\u02f8")
        buf.write("\u02ff\u0306\u030a\u030f\u0313\u0316\u031b\u0321\u032e")
        buf.write("\u0339\u033b\u034a\u034c\u0358\u035a\u0367\u0369\u037b")
        buf.write("\u037d\u0389\u038b\u0396\u03a1\u03ac\u03b7\u03c2\u03cc")
        buf.write("\u03d4\u03d8\u03de\u03eb\u03f5\u0400\u0407\u040b\u040f")
        buf.write("\u0413\u0417\u041c\u041f\u0424\u0427\u042d\u0435\u043a")
        buf.write("\u043d\u0442\u0448\u044e\u0459\u0463\u047a\u047e\u0486")
        buf.write("\u048c\u04a0\u04a4\u04b1\u04b5\u04b8\u04bf\u04c7\u04d1")
        buf.write("\u04d5\u04dd\u04e8\u04f5\u04ff\u0504\u050b\u050e\u0513")
        buf.write("\u0518\u052d\u0531\u0536\u0541\u0547\u054b\u0550\u0554")
        buf.write("\u0559\u055c\u0572\u0578\u0583\u0587\u058a\u0594\u059a")
        buf.write("\u059d\u05a4\u05ae\u05b2\u05b5\u05b8\u05bc\u05c1\u05c3")
        buf.write("\u05c7\u05cb\u05d4\u05e1\u05e9\u05ef\u05f5\u05f9\u05fc")
        buf.write("\u0605\u060e\u0616\u0621\u0627\u0632\u0635\u063a\u0649")
        buf.write("\u064f\u0658\u0662\u0668\u0670\u0674\u0678\u067d\u0682")
        buf.write("\u0689\u068b\u0690\u0694\u06a2\u06a8\u06b7\u06c1\u06c6")
        buf.write("\u06cd\u06d3\u06d8\u06de\u06e5\u06e9\u06eb\u06ed\u06f4")
        buf.write("\u06f7\u06fa\u06fd\u0702\u0706\u0709\u070d\u0711\u0716")
        buf.write("\u0719\u071b\u071f\u0726\u072c\u0730\u0736\u073b\u073d")
        buf.write("\u0743\u0747\u074d\u0754\u0758\u075a\u075c\u0763\u076d")
        buf.write("\u0771\u0773\u0775\u0779\u077c\u0782\u078c\u0790\u0796")
        buf.write("\u079e\u07a2\u07a5\u07a9\u07ae\u07b1\u07b4\u07b8\u07bd")
        buf.write("\u07c7\u07ca\u07cd\u07d1\u07dc\u07e1\u07e5\u07ea\u07f0")
        buf.write("\u07f4\u07fa\u0800\u0804\u0809\u080f\u0813\u0816\u081a")
        buf.write("\u081d\u081f\u0822\u082c\u0831\u0833\u0836\u0839\u083c")
        buf.write("\u0845\u084f\u0854\u0857\u085b\u085e\u0861\u0865\u086e")
        buf.write("\u087d\u0883\u0887\u088b\u088f\u0893\u0897\u089b\u089f")
        buf.write("\u08a2\u08a6\u08b1\u08b5\u08bc\u08c0\u08c5\u08ca\u08d1")
        buf.write("\u08d5\u08df\u08ef\u08f4\u08f8\u08fb\u08ff\u0905\u0908")
        buf.write("\u090c\u0916\u0919\u0921\u0926\u092b\u0933\u093a\u093e")
        buf.write("\u0945\u094b\u094f\u0955\u095e\u0962\u0965\u0975\u097c")
        buf.write("\u0985\u098b\u098f\u0992\u0996\u099a\u099f\u09a6\u09ac")
        buf.write("\u09b0\u09b9\u09f2\u09fb")
        return buf.getvalue()


class CPP14Parser ( Parser ):

    grammarFileName = "CPP14.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'alignas'", 
                     "'alignof'", "'asm'", "'auto'", "'bool'", "'break'", 
                     "'case'", "'catch'", "'char'", "'char16_t'", "'char32_t'", 
                     "'class'", "'const'", "'constexpr'", "'const_cast'", 
                     "'continue'", "'co_return'", "'co_yield'", "'decltype'", 
                     "'default'", "'delete'", "'do'", "'double'", "'dynamic_cast'", 
                     "'else'", "'enum'", "'explicit'", "'export'", "'extern'", 
                     "'false'", "'final'", "'float'", "'for'", "'friend'", 
                     "'goto'", "'if'", "'inline'", "'int'", "'long'", "'mutable'", 
                     "'namespace'", "'new'", "'noexcept'", "'nullptr'", 
                     "'operator'", "'override'", "'private'", "'protected'", 
                     "'public'", "'register'", "'reinterpret_cast'", "'return'", 
                     "'short'", "'signed'", "'sizeof'", "'static'", "'static_assert'", 
                     "'static_cast'", "'struct'", "'switch'", "'template'", 
                     "'this'", "'thread_local'", "'throw'", "'true'", "'try'", 
                     "'typedef'", "'typeid'", "'typename'", "'union'", "'unsigned'", 
                     "'using'", "'virtual'", "'void'", "'volatile'", "'wchar_t'", 
                     "'while'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'&'", "'|'", 
                     "'~'", "'!'", "'='", "'<'", "'>'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'^='", "'&='", "'|='", "'<<'", 
                     "'<<='", "'=='", "'!='", "'<='", "'>='", "'&&'", "'||'", 
                     "'++'", "'--'", "','", "'->*'", "'->'", "'?'", "':'", 
                     "'::'", "';'", "'.'", "'.*'", "'...'" ]

    symbolicNames = [ "<INVALID>", "MultiLineMacro", "Directive", "Alignas", 
                      "Alignof", "Asm", "Auto", "Bool", "Break", "Case", 
                      "Catch", "Char", "Char16", "Char32", "Class", "Const", 
                      "Constexpr", "Const_cast", "Continue", "CoReturn", 
                      "CoYield", "Decltype", "Default", "Delete", "Do", 
                      "Double", "Dynamic_cast", "Else", "Enum", "Explicit", 
                      "Export", "Extern", "KFalse", "Final", "Float", "For", 
                      "Friend", "Goto", "If", "Inline", "Int", "Long", "Mutable", 
                      "Namespace", "New", "Noexcept", "Nullptr", "Operator", 
                      "Override", "Private", "Protected", "Public", "Register", 
                      "Reinterpret_cast", "Return", "Short", "Signed", "Sizeof", 
                      "Static", "Static_assert", "Static_cast", "Struct", 
                      "Switch", "Template", "This", "Thread_local", "Throw", 
                      "KTrue", "Try", "Typedef", "Typeid", "Typename", "Union", 
                      "Unsigned", "Using", "Virtual", "Void", "Volatile", 
                      "Wchar", "While", "LeftParen", "RightParen", "LeftBracket", 
                      "RightBracket", "LeftBrace", "RightBrace", "Plus", 
                      "Minus", "Star", "Div", "Mod", "Caret", "And", "Or", 
                      "Tilde", "Not", "Assign", "Less", "Greater", "PlusAssign", 
                      "MinusAssign", "StarAssign", "DivAssign", "ModAssign", 
                      "XorAssign", "AndAssign", "OrAssign", "LeftShift", 
                      "LeftShiftAssign", "Equal", "NotEqual", "LessEqual", 
                      "GreaterEqual", "AndAnd", "OrOr", "PlusPlus", "MinusMinus", 
                      "Comma", "ArrowStar", "Arrow", "Question", "Colon", 
                      "Doublecolon", "Semi", "Dot", "DotStar", "Ellipsis", 
                      "Identifier", "Integerliteral", "Decimalliteral", 
                      "Octalliteral", "Hexadecimalliteral", "Binaryliteral", 
                      "Integersuffix", "Characterliteral", "Floatingliteral", 
                      "Stringliteral", "Userdefinedintegerliteral", "Userdefinedfloatingliteral", 
                      "Userdefinedstringliteral", "Userdefinedcharacterliteral", 
                      "Whitespace", "Newline", "BlockComment", "LineComment" ]

    RULE_translationunit = 0
    RULE_primaryexpression = 1
    RULE_idexpression = 2
    RULE_unqualifiedid = 3
    RULE_qualifiedid = 4
    RULE_nestednamespecifier = 5
    RULE_lambdaexpression = 6
    RULE_lambdaintroducer = 7
    RULE_lambdacapture = 8
    RULE_capturedefault = 9
    RULE_capturelist = 10
    RULE_capture = 11
    RULE_simplecapture = 12
    RULE_initcapture = 13
    RULE_lambdadeclarator = 14
    RULE_postfixexpression = 15
    RULE_expressionlist = 16
    RULE_pseudodestructorname = 17
    RULE_unaryexpression = 18
    RULE_unaryoperator = 19
    RULE_newexpression = 20
    RULE_newplacement = 21
    RULE_newtypeid = 22
    RULE_newdeclarator = 23
    RULE_noptrnewdeclarator = 24
    RULE_newinitializer = 25
    RULE_deleteexpression = 26
    RULE_noexceptexpression = 27
    RULE_castexpression = 28
    RULE_pmexpression = 29
    RULE_multiplicativeexpression = 30
    RULE_additiveexpression = 31
    RULE_shiftexpression = 32
    RULE_relationalexpression = 33
    RULE_equalityexpression = 34
    RULE_andexpression = 35
    RULE_exclusiveorexpression = 36
    RULE_inclusiveorexpression = 37
    RULE_logicalandexpression = 38
    RULE_logicalorexpression = 39
    RULE_conditionalexpression = 40
    RULE_assignmentexpression = 41
    RULE_co_assignmentexpression = 42
    RULE_yieldexpression = 43
    RULE_assignmentoperator = 44
    RULE_expression = 45
    RULE_co_expression = 46
    RULE_constantexpression = 47
    RULE_statement = 48
    RULE_co_statement = 49
    RULE_labeledstatement = 50
    RULE_expressionstatement = 51
    RULE_co_expressionstatement = 52
    RULE_compoundstatement = 53
    RULE_co_compoundstatement = 54
    RULE_statementseq = 55
    RULE_co_statementseq = 56
    RULE_selectionstatement = 57
    RULE_condition = 58
    RULE_iterationstatement = 59
    RULE_forinitstatement = 60
    RULE_forrangedeclaration = 61
    RULE_forrangeinitializer = 62
    RULE_jumpstatement = 63
    RULE_co_jumpstatement = 64
    RULE_declarationstatement = 65
    RULE_declarationseq = 66
    RULE_declaration = 67
    RULE_blockdeclaration = 68
    RULE_aliasdeclaration = 69
    RULE_simpledeclaration = 70
    RULE_static_assertdeclaration = 71
    RULE_emptydeclaration = 72
    RULE_attributedeclaration = 73
    RULE_declspecifier = 74
    RULE_declspecifierseq = 75
    RULE_storageclassspecifier = 76
    RULE_functionspecifier = 77
    RULE_typedefname = 78
    RULE_typespecifier = 79
    RULE_trailingtypespecifier = 80
    RULE_typespecifierseq = 81
    RULE_trailingtypespecifierseq = 82
    RULE_simpletypespecifier = 83
    RULE_typename = 84
    RULE_decltypespecifier = 85
    RULE_elaboratedtypespecifier = 86
    RULE_enumname = 87
    RULE_enumspecifier = 88
    RULE_enumhead = 89
    RULE_opaqueenumdeclaration = 90
    RULE_enumkey = 91
    RULE_enumbase = 92
    RULE_enumeratorlist = 93
    RULE_enumeratordefinition = 94
    RULE_enumerator = 95
    RULE_namespacename = 96
    RULE_originalnamespacename = 97
    RULE_namespacedefinition = 98
    RULE_namednamespacedefinition = 99
    RULE_originalnamespacedefinition = 100
    RULE_extensionnamespacedefinition = 101
    RULE_unnamednamespacedefinition = 102
    RULE_namespacebody = 103
    RULE_namespacealias = 104
    RULE_namespacealiasdefinition = 105
    RULE_qualifiednamespacespecifier = 106
    RULE_usingdeclaration = 107
    RULE_usingdirective = 108
    RULE_asmdefinition = 109
    RULE_linkagespecification = 110
    RULE_attributespecifierseq = 111
    RULE_attributespecifier = 112
    RULE_alignmentspecifier = 113
    RULE_attributelist = 114
    RULE_attribute = 115
    RULE_attributetoken = 116
    RULE_attributescopedtoken = 117
    RULE_attributenamespace = 118
    RULE_attributeargumentclause = 119
    RULE_balancedtokenseq = 120
    RULE_balancedtoken = 121
    RULE_initdeclaratorlist = 122
    RULE_initdeclarator = 123
    RULE_declarator = 124
    RULE_ptrdeclarator = 125
    RULE_noptrdeclarator = 126
    RULE_parametersandqualifiers = 127
    RULE_trailingreturntype = 128
    RULE_ptroperator = 129
    RULE_cvqualifierseq = 130
    RULE_cvqualifier = 131
    RULE_refqualifier = 132
    RULE_declaratorid = 133
    RULE_typeid = 134
    RULE_abstractdeclarator = 135
    RULE_ptrabstractdeclarator = 136
    RULE_noptrabstractdeclarator = 137
    RULE_abstractpackdeclarator = 138
    RULE_noptrabstractpackdeclarator = 139
    RULE_parameterdeclarationclause = 140
    RULE_parameterdeclarationlist = 141
    RULE_parameterdeclaration = 142
    RULE_functiondefinition = 143
    RULE_functionbody = 144
    RULE_coroutinedefinition = 145
    RULE_coroutinebody = 146
    RULE_initializer = 147
    RULE_braceorequalinitializer = 148
    RULE_initializerclause = 149
    RULE_initializerlist = 150
    RULE_bracedinitlist = 151
    RULE_classname = 152
    RULE_classspecifier = 153
    RULE_classhead = 154
    RULE_classheadname = 155
    RULE_classvirtspecifier = 156
    RULE_classkey = 157
    RULE_memberspecification = 158
    RULE_memberdeclaration = 159
    RULE_memberdeclaratorlist = 160
    RULE_memberdeclarator = 161
    RULE_virtspecifierseq = 162
    RULE_virtspecifier = 163
    RULE_purespecifier = 164
    RULE_baseclause = 165
    RULE_basespecifierlist = 166
    RULE_basespecifier = 167
    RULE_classordecltype = 168
    RULE_basetypespecifier = 169
    RULE_accessspecifier = 170
    RULE_conversionfunctionid = 171
    RULE_conversiontypeid = 172
    RULE_conversiondeclarator = 173
    RULE_ctorinitializer = 174
    RULE_meminitializerlist = 175
    RULE_meminitializer = 176
    RULE_meminitializerid = 177
    RULE_operatorfunctionid = 178
    RULE_literaloperatorid = 179
    RULE_templatedeclaration = 180
    RULE_templateparameterlist = 181
    RULE_templateparameter = 182
    RULE_typeparameter = 183
    RULE_simpletemplateid = 184
    RULE_templateid = 185
    RULE_templatename = 186
    RULE_templateargumentlist = 187
    RULE_templateargument = 188
    RULE_typenamespecifier = 189
    RULE_explicitinstantiation = 190
    RULE_explicitspecialization = 191
    RULE_tryblock = 192
    RULE_functiontryblock = 193
    RULE_handlerseq = 194
    RULE_handler = 195
    RULE_exceptiondeclaration = 196
    RULE_throwexpression = 197
    RULE_exceptionspecification = 198
    RULE_dynamicexceptionspecification = 199
    RULE_typeidlist = 200
    RULE_noexceptspecification = 201
    RULE_rightShift = 202
    RULE_rightShiftAssign = 203
    RULE_operator = 204
    RULE_literal = 205
    RULE_booleanliteral = 206
    RULE_pointerliteral = 207
    RULE_userdefinedliteral = 208

    ruleNames =  [ "translationunit", "primaryexpression", "idexpression", 
                   "unqualifiedid", "qualifiedid", "nestednamespecifier", 
                   "lambdaexpression", "lambdaintroducer", "lambdacapture", 
                   "capturedefault", "capturelist", "capture", "simplecapture", 
                   "initcapture", "lambdadeclarator", "postfixexpression", 
                   "expressionlist", "pseudodestructorname", "unaryexpression", 
                   "unaryoperator", "newexpression", "newplacement", "newtypeid", 
                   "newdeclarator", "noptrnewdeclarator", "newinitializer", 
                   "deleteexpression", "noexceptexpression", "castexpression", 
                   "pmexpression", "multiplicativeexpression", "additiveexpression", 
                   "shiftexpression", "relationalexpression", "equalityexpression", 
                   "andexpression", "exclusiveorexpression", "inclusiveorexpression", 
                   "logicalandexpression", "logicalorexpression", "conditionalexpression", 
                   "assignmentexpression", "co_assignmentexpression", "yieldexpression", 
                   "assignmentoperator", "expression", "co_expression", 
                   "constantexpression", "statement", "co_statement", "labeledstatement", 
                   "expressionstatement", "co_expressionstatement", "compoundstatement", 
                   "co_compoundstatement", "statementseq", "co_statementseq", 
                   "selectionstatement", "condition", "iterationstatement", 
                   "forinitstatement", "forrangedeclaration", "forrangeinitializer", 
                   "jumpstatement", "co_jumpstatement", "declarationstatement", 
                   "declarationseq", "declaration", "blockdeclaration", 
                   "aliasdeclaration", "simpledeclaration", "static_assertdeclaration", 
                   "emptydeclaration", "attributedeclaration", "declspecifier", 
                   "declspecifierseq", "storageclassspecifier", "functionspecifier", 
                   "typedefname", "typespecifier", "trailingtypespecifier", 
                   "typespecifierseq", "trailingtypespecifierseq", "simpletypespecifier", 
                   "typename", "decltypespecifier", "elaboratedtypespecifier", 
                   "enumname", "enumspecifier", "enumhead", "opaqueenumdeclaration", 
                   "enumkey", "enumbase", "enumeratorlist", "enumeratordefinition", 
                   "enumerator", "namespacename", "originalnamespacename", 
                   "namespacedefinition", "namednamespacedefinition", "originalnamespacedefinition", 
                   "extensionnamespacedefinition", "unnamednamespacedefinition", 
                   "namespacebody", "namespacealias", "namespacealiasdefinition", 
                   "qualifiednamespacespecifier", "usingdeclaration", "usingdirective", 
                   "asmdefinition", "linkagespecification", "attributespecifierseq", 
                   "attributespecifier", "alignmentspecifier", "attributelist", 
                   "attribute", "attributetoken", "attributescopedtoken", 
                   "attributenamespace", "attributeargumentclause", "balancedtokenseq", 
                   "balancedtoken", "initdeclaratorlist", "initdeclarator", 
                   "declarator", "ptrdeclarator", "noptrdeclarator", "parametersandqualifiers", 
                   "trailingreturntype", "ptroperator", "cvqualifierseq", 
                   "cvqualifier", "refqualifier", "declaratorid", "typeid", 
                   "abstractdeclarator", "ptrabstractdeclarator", "noptrabstractdeclarator", 
                   "abstractpackdeclarator", "noptrabstractpackdeclarator", 
                   "parameterdeclarationclause", "parameterdeclarationlist", 
                   "parameterdeclaration", "functiondefinition", "functionbody", 
                   "coroutinedefinition", "coroutinebody", "initializer", 
                   "braceorequalinitializer", "initializerclause", "initializerlist", 
                   "bracedinitlist", "classname", "classspecifier", "classhead", 
                   "classheadname", "classvirtspecifier", "classkey", "memberspecification", 
                   "memberdeclaration", "memberdeclaratorlist", "memberdeclarator", 
                   "virtspecifierseq", "virtspecifier", "purespecifier", 
                   "baseclause", "basespecifierlist", "basespecifier", "classordecltype", 
                   "basetypespecifier", "accessspecifier", "conversionfunctionid", 
                   "conversiontypeid", "conversiondeclarator", "ctorinitializer", 
                   "meminitializerlist", "meminitializer", "meminitializerid", 
                   "operatorfunctionid", "literaloperatorid", "templatedeclaration", 
                   "templateparameterlist", "templateparameter", "typeparameter", 
                   "simpletemplateid", "templateid", "templatename", "templateargumentlist", 
                   "templateargument", "typenamespecifier", "explicitinstantiation", 
                   "explicitspecialization", "tryblock", "functiontryblock", 
                   "handlerseq", "handler", "exceptiondeclaration", "throwexpression", 
                   "exceptionspecification", "dynamicexceptionspecification", 
                   "typeidlist", "noexceptspecification", "rightShift", 
                   "rightShiftAssign", "operator", "literal", "booleanliteral", 
                   "pointerliteral", "userdefinedliteral" ]

    EOF = Token.EOF
    MultiLineMacro=1
    Directive=2
    Alignas=3
    Alignof=4
    Asm=5
    Auto=6
    Bool=7
    Break=8
    Case=9
    Catch=10
    Char=11
    Char16=12
    Char32=13
    Class=14
    Const=15
    Constexpr=16
    Const_cast=17
    Continue=18
    CoReturn=19
    CoYield=20
    Decltype=21
    Default=22
    Delete=23
    Do=24
    Double=25
    Dynamic_cast=26
    Else=27
    Enum=28
    Explicit=29
    Export=30
    Extern=31
    KFalse=32
    Final=33
    Float=34
    For=35
    Friend=36
    Goto=37
    If=38
    Inline=39
    Int=40
    Long=41
    Mutable=42
    Namespace=43
    New=44
    Noexcept=45
    Nullptr=46
    Operator=47
    Override=48
    Private=49
    Protected=50
    Public=51
    Register=52
    Reinterpret_cast=53
    Return=54
    Short=55
    Signed=56
    Sizeof=57
    Static=58
    Static_assert=59
    Static_cast=60
    Struct=61
    Switch=62
    Template=63
    This=64
    Thread_local=65
    Throw=66
    KTrue=67
    Try=68
    Typedef=69
    Typeid=70
    Typename=71
    Union=72
    Unsigned=73
    Using=74
    Virtual=75
    Void=76
    Volatile=77
    Wchar=78
    While=79
    LeftParen=80
    RightParen=81
    LeftBracket=82
    RightBracket=83
    LeftBrace=84
    RightBrace=85
    Plus=86
    Minus=87
    Star=88
    Div=89
    Mod=90
    Caret=91
    And=92
    Or=93
    Tilde=94
    Not=95
    Assign=96
    Less=97
    Greater=98
    PlusAssign=99
    MinusAssign=100
    StarAssign=101
    DivAssign=102
    ModAssign=103
    XorAssign=104
    AndAssign=105
    OrAssign=106
    LeftShift=107
    LeftShiftAssign=108
    Equal=109
    NotEqual=110
    LessEqual=111
    GreaterEqual=112
    AndAnd=113
    OrOr=114
    PlusPlus=115
    MinusMinus=116
    Comma=117
    ArrowStar=118
    Arrow=119
    Question=120
    Colon=121
    Doublecolon=122
    Semi=123
    Dot=124
    DotStar=125
    Ellipsis=126
    Identifier=127
    Integerliteral=128
    Decimalliteral=129
    Octalliteral=130
    Hexadecimalliteral=131
    Binaryliteral=132
    Integersuffix=133
    Characterliteral=134
    Floatingliteral=135
    Stringliteral=136
    Userdefinedintegerliteral=137
    Userdefinedfloatingliteral=138
    Userdefinedstringliteral=139
    Userdefinedcharacterliteral=140
    Whitespace=141
    Newline=142
    BlockComment=143
    LineComment=144

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TranslationunitContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CPP14Parser.EOF, 0)

        def declarationseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_translationunit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationunit" ):
                listener.enterTranslationunit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationunit" ):
                listener.exitTranslationunit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslationunit" ):
                return visitor.visitTranslationunit(self)
            else:
                return visitor.visitChildren(self)




    def translationunit(self):

        localctx = CPP14Parser.TranslationunitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_translationunit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Asm) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Namespace) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Template))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Using - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftParen - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Star - 65)) | (1 << (CPP14Parser.And - 65)) | (1 << (CPP14Parser.Tilde - 65)) | (1 << (CPP14Parser.AndAnd - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Semi - 65)) | (1 << (CPP14Parser.Ellipsis - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                self.state = 418
                self.declarationseq(0)


            self.state = 421
            self.match(CPP14Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CPP14Parser.LiteralContext,0)


        def This(self):
            return self.getToken(CPP14Parser.This, 0)

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def idexpression(self):
            return self.getTypedRuleContext(CPP14Parser.IdexpressionContext,0)


        def lambdaexpression(self):
            return self.getTypedRuleContext(CPP14Parser.LambdaexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_primaryexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryexpression" ):
                listener.enterPrimaryexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryexpression" ):
                listener.exitPrimaryexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryexpression" ):
                return visitor.visitPrimaryexpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryexpression(self):

        localctx = CPP14Parser.PrimaryexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primaryexpression)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.KFalse, CPP14Parser.Nullptr, CPP14Parser.KTrue, CPP14Parser.Integerliteral, CPP14Parser.Characterliteral, CPP14Parser.Floatingliteral, CPP14Parser.Stringliteral, CPP14Parser.Userdefinedintegerliteral, CPP14Parser.Userdefinedfloatingliteral, CPP14Parser.Userdefinedstringliteral, CPP14Parser.Userdefinedcharacterliteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.literal()
                pass
            elif token in [CPP14Parser.This]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(CPP14Parser.This)
                pass
            elif token in [CPP14Parser.LeftParen]:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.match(CPP14Parser.LeftParen)
                self.state = 426
                self.expression(0)
                self.state = 427
                self.match(CPP14Parser.RightParen)
                pass
            elif token in [CPP14Parser.Decltype, CPP14Parser.Operator, CPP14Parser.Tilde, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 429
                self.idexpression()
                pass
            elif token in [CPP14Parser.LeftBracket]:
                self.enterOuterAlt(localctx, 5)
                self.state = 430
                self.lambdaexpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unqualifiedid(self):
            return self.getTypedRuleContext(CPP14Parser.UnqualifiedidContext,0)


        def qualifiedid(self):
            return self.getTypedRuleContext(CPP14Parser.QualifiedidContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_idexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdexpression" ):
                listener.enterIdexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdexpression" ):
                listener.exitIdexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdexpression" ):
                return visitor.visitIdexpression(self)
            else:
                return visitor.visitChildren(self)




    def idexpression(self):

        localctx = CPP14Parser.IdexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_idexpression)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.unqualifiedid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.qualifiedid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnqualifiedidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def operatorfunctionid(self):
            return self.getTypedRuleContext(CPP14Parser.OperatorfunctionidContext,0)


        def conversionfunctionid(self):
            return self.getTypedRuleContext(CPP14Parser.ConversionfunctionidContext,0)


        def literaloperatorid(self):
            return self.getTypedRuleContext(CPP14Parser.LiteraloperatoridContext,0)


        def classname(self):
            return self.getTypedRuleContext(CPP14Parser.ClassnameContext,0)


        def decltypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.DecltypespecifierContext,0)


        def templateid(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateidContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_unqualifiedid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnqualifiedid" ):
                listener.enterUnqualifiedid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnqualifiedid" ):
                listener.exitUnqualifiedid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnqualifiedid" ):
                return visitor.visitUnqualifiedid(self)
            else:
                return visitor.visitChildren(self)




    def unqualifiedid(self):

        localctx = CPP14Parser.UnqualifiedidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_unqualifiedid)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.operatorfunctionid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 439
                self.conversionfunctionid()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 440
                self.literaloperatorid()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 441
                self.match(CPP14Parser.Tilde)
                self.state = 442
                self.classname()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 443
                self.match(CPP14Parser.Tilde)
                self.state = 444
                self.decltypespecifier()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 445
                self.templateid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QualifiedidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def unqualifiedid(self):
            return self.getTypedRuleContext(CPP14Parser.UnqualifiedidContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_qualifiedid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedid" ):
                listener.enterQualifiedid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedid" ):
                listener.exitQualifiedid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedid" ):
                return visitor.visitQualifiedid(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedid(self):

        localctx = CPP14Parser.QualifiedidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_qualifiedid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.nestednamespecifier(0)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Template:
                self.state = 449
                self.match(CPP14Parser.Template)


            self.state = 452
            self.unqualifiedid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NestednamespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(CPP14Parser.TypenameContext,0)


        def namespacename(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacenameContext,0)


        def decltypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.DecltypespecifierContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_nestednamespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestednamespecifier" ):
                listener.enterNestednamespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestednamespecifier" ):
                listener.exitNestednamespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestednamespecifier" ):
                return visitor.visitNestednamespecifier(self)
            else:
                return visitor.visitChildren(self)



    def nestednamespecifier(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.NestednamespecifierContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_nestednamespecifier, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 455
                self.match(CPP14Parser.Doublecolon)
                pass

            elif la_ == 2:
                self.state = 456
                self.typename()
                self.state = 457
                self.match(CPP14Parser.Doublecolon)
                pass

            elif la_ == 3:
                self.state = 459
                self.namespacename()
                self.state = 460
                self.match(CPP14Parser.Doublecolon)
                pass

            elif la_ == 4:
                self.state = 462
                self.decltypespecifier()
                self.state = 463
                self.match(CPP14Parser.Doublecolon)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 477
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.NestednamespecifierContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_nestednamespecifier)
                        self.state = 467
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 468
                        self.match(CPP14Parser.Identifier)
                        self.state = 469
                        self.match(CPP14Parser.Doublecolon)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.NestednamespecifierContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_nestednamespecifier)
                        self.state = 470
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 472
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CPP14Parser.Template:
                            self.state = 471
                            self.match(CPP14Parser.Template)


                        self.state = 474
                        self.simpletemplateid()
                        self.state = 475
                        self.match(CPP14Parser.Doublecolon)
                        pass

             
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LambdaexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaintroducer(self):
            return self.getTypedRuleContext(CPP14Parser.LambdaintroducerContext,0)


        def compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.CompoundstatementContext,0)


        def lambdadeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.LambdadeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_lambdaexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaexpression" ):
                listener.enterLambdaexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaexpression" ):
                listener.exitLambdaexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaexpression" ):
                return visitor.visitLambdaexpression(self)
            else:
                return visitor.visitChildren(self)




    def lambdaexpression(self):

        localctx = CPP14Parser.LambdaexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lambdaexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.lambdaintroducer()
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.LeftParen:
                self.state = 483
                self.lambdadeclarator()


            self.state = 486
            self.compoundstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LambdaintroducerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdacapture(self):
            return self.getTypedRuleContext(CPP14Parser.LambdacaptureContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_lambdaintroducer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaintroducer" ):
                listener.enterLambdaintroducer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaintroducer" ):
                listener.exitLambdaintroducer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaintroducer" ):
                return visitor.visitLambdaintroducer(self)
            else:
                return visitor.visitChildren(self)




    def lambdaintroducer(self):

        localctx = CPP14Parser.LambdaintroducerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lambdaintroducer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(CPP14Parser.LeftBracket)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Assign - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0):
                self.state = 489
                self.lambdacapture()


            self.state = 492
            self.match(CPP14Parser.RightBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LambdacaptureContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capturedefault(self):
            return self.getTypedRuleContext(CPP14Parser.CapturedefaultContext,0)


        def capturelist(self):
            return self.getTypedRuleContext(CPP14Parser.CapturelistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_lambdacapture

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdacapture" ):
                listener.enterLambdacapture(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdacapture" ):
                listener.exitLambdacapture(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdacapture" ):
                return visitor.visitLambdacapture(self)
            else:
                return visitor.visitChildren(self)




    def lambdacapture(self):

        localctx = CPP14Parser.LambdacaptureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lambdacapture)
        try:
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.capturedefault()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.capturelist(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.capturedefault()
                self.state = 497
                self.match(CPP14Parser.Comma)
                self.state = 498
                self.capturelist(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CapturedefaultContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPP14Parser.RULE_capturedefault

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapturedefault" ):
                listener.enterCapturedefault(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapturedefault" ):
                listener.exitCapturedefault(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapturedefault" ):
                return visitor.visitCapturedefault(self)
            else:
                return visitor.visitChildren(self)




    def capturedefault(self):

        localctx = CPP14Parser.CapturedefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_capturedefault)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            _la = self._input.LA(1)
            if not(_la==CPP14Parser.And or _la==CPP14Parser.Assign):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CapturelistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capture(self):
            return self.getTypedRuleContext(CPP14Parser.CaptureContext,0)


        def capturelist(self):
            return self.getTypedRuleContext(CPP14Parser.CapturelistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_capturelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapturelist" ):
                listener.enterCapturelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapturelist" ):
                listener.exitCapturelist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapturelist" ):
                return visitor.visitCapturelist(self)
            else:
                return visitor.visitChildren(self)



    def capturelist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.CapturelistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_capturelist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.capture()
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 506
                self.match(CPP14Parser.Ellipsis)


            self._ctx.stop = self._input.LT(-1)
            self.state = 517
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.CapturelistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_capturelist)
                    self.state = 509
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 510
                    self.match(CPP14Parser.Comma)
                    self.state = 511
                    self.capture()
                    self.state = 513
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 512
                        self.match(CPP14Parser.Ellipsis)

             
                self.state = 519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CaptureContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simplecapture(self):
            return self.getTypedRuleContext(CPP14Parser.SimplecaptureContext,0)


        def initcapture(self):
            return self.getTypedRuleContext(CPP14Parser.InitcaptureContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_capture

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapture" ):
                listener.enterCapture(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapture" ):
                listener.exitCapture(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapture" ):
                return visitor.visitCapture(self)
            else:
                return visitor.visitChildren(self)




    def capture(self):

        localctx = CPP14Parser.CaptureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_capture)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.simplecapture()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.initcapture()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimplecaptureContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def This(self):
            return self.getToken(CPP14Parser.This, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_simplecapture

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimplecapture" ):
                listener.enterSimplecapture(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimplecapture" ):
                listener.exitSimplecapture(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimplecapture" ):
                return visitor.visitSimplecapture(self)
            else:
                return visitor.visitChildren(self)




    def simplecapture(self):

        localctx = CPP14Parser.SimplecaptureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_simplecapture)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(CPP14Parser.Identifier)
                pass
            elif token in [CPP14Parser.And]:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.match(CPP14Parser.And)
                self.state = 526
                self.match(CPP14Parser.Identifier)
                pass
            elif token in [CPP14Parser.This]:
                self.enterOuterAlt(localctx, 3)
                self.state = 527
                self.match(CPP14Parser.This)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitcaptureContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def initializer(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_initcapture

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitcapture" ):
                listener.enterInitcapture(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitcapture" ):
                listener.exitInitcapture(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitcapture" ):
                return visitor.visitInitcapture(self)
            else:
                return visitor.visitChildren(self)




    def initcapture(self):

        localctx = CPP14Parser.InitcaptureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_initcapture)
        try:
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(CPP14Parser.Identifier)
                self.state = 531
                self.initializer()
                pass
            elif token in [CPP14Parser.And]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(CPP14Parser.And)
                self.state = 533
                self.match(CPP14Parser.Identifier)
                self.state = 534
                self.initializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LambdadeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterdeclarationclause(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterdeclarationclauseContext,0)


        def Mutable(self):
            return self.getToken(CPP14Parser.Mutable, 0)

        def exceptionspecification(self):
            return self.getTypedRuleContext(CPP14Parser.ExceptionspecificationContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def trailingreturntype(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingreturntypeContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_lambdadeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdadeclarator" ):
                listener.enterLambdadeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdadeclarator" ):
                listener.exitLambdadeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdadeclarator" ):
                return visitor.visitLambdadeclarator(self)
            else:
                return visitor.visitChildren(self)




    def lambdadeclarator(self):

        localctx = CPP14Parser.LambdadeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lambdadeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(CPP14Parser.LeftParen)
            self.state = 538
            self.parameterdeclarationclause()
            self.state = 539
            self.match(CPP14Parser.RightParen)
            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Mutable:
                self.state = 540
                self.match(CPP14Parser.Mutable)


            self.state = 544
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Noexcept or _la==CPP14Parser.Throw:
                self.state = 543
                self.exceptionspecification()


            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 546
                self.attributespecifierseq(0)


            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Arrow:
                self.state = 549
                self.trailingreturntype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PostfixexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryexpression(self):
            return self.getTypedRuleContext(CPP14Parser.PrimaryexpressionContext,0)


        def simpletypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletypespecifierContext,0)


        def expressionlist(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionlistContext,0)


        def typenamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.TypenamespecifierContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def Dynamic_cast(self):
            return self.getToken(CPP14Parser.Dynamic_cast, 0)

        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def Static_cast(self):
            return self.getToken(CPP14Parser.Static_cast, 0)

        def Reinterpret_cast(self):
            return self.getToken(CPP14Parser.Reinterpret_cast, 0)

        def Const_cast(self):
            return self.getToken(CPP14Parser.Const_cast, 0)

        def Typeid(self):
            return self.getToken(CPP14Parser.Typeid, 0)

        def postfixexpression(self):
            return self.getTypedRuleContext(CPP14Parser.PostfixexpressionContext,0)


        def idexpression(self):
            return self.getTypedRuleContext(CPP14Parser.IdexpressionContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def pseudodestructorname(self):
            return self.getTypedRuleContext(CPP14Parser.PseudodestructornameContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_postfixexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixexpression" ):
                listener.enterPostfixexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixexpression" ):
                listener.exitPostfixexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixexpression" ):
                return visitor.visitPostfixexpression(self)
            else:
                return visitor.visitChildren(self)



    def postfixexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.PostfixexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_postfixexpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 553
                self.primaryexpression()
                pass

            elif la_ == 2:
                self.state = 554
                self.simpletypespecifier()
                self.state = 555
                self.match(CPP14Parser.LeftParen)
                self.state = 557
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 556
                    self.expressionlist()


                self.state = 559
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 3:
                self.state = 561
                self.typenamespecifier()
                self.state = 562
                self.match(CPP14Parser.LeftParen)
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 563
                    self.expressionlist()


                self.state = 566
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 4:
                self.state = 568
                self.simpletypespecifier()
                self.state = 569
                self.bracedinitlist()
                pass

            elif la_ == 5:
                self.state = 571
                self.typenamespecifier()
                self.state = 572
                self.bracedinitlist()
                pass

            elif la_ == 6:
                self.state = 574
                self.match(CPP14Parser.Dynamic_cast)
                self.state = 575
                self.match(CPP14Parser.Less)
                self.state = 576
                self.typeid()
                self.state = 577
                self.match(CPP14Parser.Greater)
                self.state = 578
                self.match(CPP14Parser.LeftParen)
                self.state = 579
                self.expression(0)
                self.state = 580
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 7:
                self.state = 582
                self.match(CPP14Parser.Static_cast)
                self.state = 583
                self.match(CPP14Parser.Less)
                self.state = 584
                self.typeid()
                self.state = 585
                self.match(CPP14Parser.Greater)
                self.state = 586
                self.match(CPP14Parser.LeftParen)
                self.state = 587
                self.expression(0)
                self.state = 588
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 8:
                self.state = 590
                self.match(CPP14Parser.Reinterpret_cast)
                self.state = 591
                self.match(CPP14Parser.Less)
                self.state = 592
                self.typeid()
                self.state = 593
                self.match(CPP14Parser.Greater)
                self.state = 594
                self.match(CPP14Parser.LeftParen)
                self.state = 595
                self.expression(0)
                self.state = 596
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 9:
                self.state = 598
                self.match(CPP14Parser.Const_cast)
                self.state = 599
                self.match(CPP14Parser.Less)
                self.state = 600
                self.typeid()
                self.state = 601
                self.match(CPP14Parser.Greater)
                self.state = 602
                self.match(CPP14Parser.LeftParen)
                self.state = 603
                self.expression(0)
                self.state = 604
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 10:
                self.state = 606
                self.match(CPP14Parser.Typeid)
                self.state = 607
                self.match(CPP14Parser.LeftParen)
                self.state = 608
                self.expression(0)
                self.state = 609
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 11:
                self.state = 611
                self.match(CPP14Parser.Typeid)
                self.state = 612
                self.match(CPP14Parser.LeftParen)
                self.state = 613
                self.typeid()
                self.state = 614
                self.match(CPP14Parser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 658
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 656
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 618
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 619
                        self.match(CPP14Parser.LeftBracket)
                        self.state = 620
                        self.expression(0)
                        self.state = 621
                        self.match(CPP14Parser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 623
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 624
                        self.match(CPP14Parser.LeftBracket)
                        self.state = 625
                        self.bracedinitlist()
                        self.state = 626
                        self.match(CPP14Parser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 628
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 629
                        self.match(CPP14Parser.LeftParen)
                        self.state = 631
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                            self.state = 630
                            self.expressionlist()


                        self.state = 633
                        self.match(CPP14Parser.RightParen)
                        pass

                    elif la_ == 4:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 634
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 635
                        self.match(CPP14Parser.Dot)
                        self.state = 637
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CPP14Parser.Template:
                            self.state = 636
                            self.match(CPP14Parser.Template)


                        self.state = 639
                        self.idexpression()
                        pass

                    elif la_ == 5:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 640
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 641
                        self.match(CPP14Parser.Arrow)
                        self.state = 643
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==CPP14Parser.Template:
                            self.state = 642
                            self.match(CPP14Parser.Template)


                        self.state = 645
                        self.idexpression()
                        pass

                    elif la_ == 6:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 646
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 647
                        self.match(CPP14Parser.Dot)
                        self.state = 648
                        self.pseudodestructorname()
                        pass

                    elif la_ == 7:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 649
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 650
                        self.match(CPP14Parser.Arrow)
                        self.state = 651
                        self.pseudodestructorname()
                        pass

                    elif la_ == 8:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 652
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 653
                        self.match(CPP14Parser.PlusPlus)
                        pass

                    elif la_ == 9:
                        localctx = CPP14Parser.PostfixexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixexpression)
                        self.state = 654
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 655
                        self.match(CPP14Parser.MinusMinus)
                        pass

             
                self.state = 660
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExpressionlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializerlist(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_expressionlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionlist" ):
                listener.enterExpressionlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionlist" ):
                listener.exitExpressionlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionlist" ):
                return visitor.visitExpressionlist(self)
            else:
                return visitor.visitChildren(self)




    def expressionlist(self):

        localctx = CPP14Parser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressionlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.initializerlist(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PseudodestructornameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPP14Parser.TypenameContext)
            else:
                return self.getTypedRuleContext(CPP14Parser.TypenameContext,i)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def decltypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.DecltypespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_pseudodestructorname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPseudodestructorname" ):
                listener.enterPseudodestructorname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPseudodestructorname" ):
                listener.exitPseudodestructorname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPseudodestructorname" ):
                return visitor.visitPseudodestructorname(self)
            else:
                return visitor.visitChildren(self)




    def pseudodestructorname(self):

        localctx = CPP14Parser.PseudodestructornameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pseudodestructorname)
        self._la = 0 # Token type
        try:
            self.state = 685
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 664
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 663
                    self.nestednamespecifier(0)


                self.state = 666
                self.typename()
                self.state = 667
                self.match(CPP14Parser.Doublecolon)
                self.state = 668
                self.match(CPP14Parser.Tilde)
                self.state = 669
                self.typename()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.nestednamespecifier(0)
                self.state = 672
                self.match(CPP14Parser.Template)
                self.state = 673
                self.simpletemplateid()
                self.state = 674
                self.match(CPP14Parser.Doublecolon)
                self.state = 675
                self.match(CPP14Parser.Tilde)
                self.state = 676
                self.typename()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 679
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Decltype or _la==CPP14Parser.Doublecolon or _la==CPP14Parser.Identifier:
                    self.state = 678
                    self.nestednamespecifier(0)


                self.state = 681
                self.match(CPP14Parser.Tilde)
                self.state = 682
                self.typename()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 683
                self.match(CPP14Parser.Tilde)
                self.state = 684
                self.decltypespecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixexpression(self):
            return self.getTypedRuleContext(CPP14Parser.PostfixexpressionContext,0)


        def castexpression(self):
            return self.getTypedRuleContext(CPP14Parser.CastexpressionContext,0)


        def unaryoperator(self):
            return self.getTypedRuleContext(CPP14Parser.UnaryoperatorContext,0)


        def Sizeof(self):
            return self.getToken(CPP14Parser.Sizeof, 0)

        def unaryexpression(self):
            return self.getTypedRuleContext(CPP14Parser.UnaryexpressionContext,0)


        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def Alignof(self):
            return self.getToken(CPP14Parser.Alignof, 0)

        def noexceptexpression(self):
            return self.getTypedRuleContext(CPP14Parser.NoexceptexpressionContext,0)


        def newexpression(self):
            return self.getTypedRuleContext(CPP14Parser.NewexpressionContext,0)


        def deleteexpression(self):
            return self.getTypedRuleContext(CPP14Parser.DeleteexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_unaryexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryexpression" ):
                listener.enterUnaryexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryexpression" ):
                listener.exitUnaryexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryexpression" ):
                return visitor.visitUnaryexpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryexpression(self):

        localctx = CPP14Parser.UnaryexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryexpression)
        try:
            self.state = 715
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 687
                self.postfixexpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 688
                self.match(CPP14Parser.PlusPlus)
                self.state = 689
                self.castexpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 690
                self.match(CPP14Parser.MinusMinus)
                self.state = 691
                self.castexpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 692
                self.unaryoperator()
                self.state = 693
                self.castexpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 695
                self.match(CPP14Parser.Sizeof)
                self.state = 696
                self.unaryexpression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 697
                self.match(CPP14Parser.Sizeof)
                self.state = 698
                self.match(CPP14Parser.LeftParen)
                self.state = 699
                self.typeid()
                self.state = 700
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 702
                self.match(CPP14Parser.Sizeof)
                self.state = 703
                self.match(CPP14Parser.Ellipsis)
                self.state = 704
                self.match(CPP14Parser.LeftParen)
                self.state = 705
                self.match(CPP14Parser.Identifier)
                self.state = 706
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 707
                self.match(CPP14Parser.Alignof)
                self.state = 708
                self.match(CPP14Parser.LeftParen)
                self.state = 709
                self.typeid()
                self.state = 710
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 712
                self.noexceptexpression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 713
                self.newexpression()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 714
                self.deleteexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryoperatorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPP14Parser.RULE_unaryoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryoperator" ):
                listener.enterUnaryoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryoperator" ):
                listener.exitUnaryoperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryoperator" ):
                return visitor.visitUnaryoperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryoperator(self):

        localctx = CPP14Parser.UnaryoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            _la = self._input.LA(1)
            if not(((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & ((1 << (CPP14Parser.Plus - 86)) | (1 << (CPP14Parser.Minus - 86)) | (1 << (CPP14Parser.Star - 86)) | (1 << (CPP14Parser.And - 86)) | (1 << (CPP14Parser.Or - 86)) | (1 << (CPP14Parser.Tilde - 86)) | (1 << (CPP14Parser.Not - 86)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def New(self):
            return self.getToken(CPP14Parser.New, 0)

        def newtypeid(self):
            return self.getTypedRuleContext(CPP14Parser.NewtypeidContext,0)


        def newplacement(self):
            return self.getTypedRuleContext(CPP14Parser.NewplacementContext,0)


        def newinitializer(self):
            return self.getTypedRuleContext(CPP14Parser.NewinitializerContext,0)


        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_newexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewexpression" ):
                listener.enterNewexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewexpression" ):
                listener.exitNewexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewexpression" ):
                return visitor.visitNewexpression(self)
            else:
                return visitor.visitChildren(self)




    def newexpression(self):

        localctx = CPP14Parser.NewexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_newexpression)
        self._la = 0 # Token type
        try:
            self.state = 743
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 720
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Doublecolon:
                    self.state = 719
                    self.match(CPP14Parser.Doublecolon)


                self.state = 722
                self.match(CPP14Parser.New)
                self.state = 724
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.LeftParen:
                    self.state = 723
                    self.newplacement()


                self.state = 726
                self.newtypeid()
                self.state = 728
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 727
                    self.newinitializer()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 731
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Doublecolon:
                    self.state = 730
                    self.match(CPP14Parser.Doublecolon)


                self.state = 733
                self.match(CPP14Parser.New)
                self.state = 735
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 734
                    self.newplacement()


                self.state = 737
                self.match(CPP14Parser.LeftParen)
                self.state = 738
                self.typeid()
                self.state = 739
                self.match(CPP14Parser.RightParen)
                self.state = 741
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 740
                    self.newinitializer()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewplacementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionlist(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_newplacement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewplacement" ):
                listener.enterNewplacement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewplacement" ):
                listener.exitNewplacement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewplacement" ):
                return visitor.visitNewplacement(self)
            else:
                return visitor.visitChildren(self)




    def newplacement(self):

        localctx = CPP14Parser.NewplacementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_newplacement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 745
            self.match(CPP14Parser.LeftParen)
            self.state = 746
            self.expressionlist()
            self.state = 747
            self.match(CPP14Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewtypeidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierseqContext,0)


        def newdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NewdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_newtypeid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewtypeid" ):
                listener.enterNewtypeid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewtypeid" ):
                listener.exitNewtypeid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewtypeid" ):
                return visitor.visitNewtypeid(self)
            else:
                return visitor.visitChildren(self)




    def newtypeid(self):

        localctx = CPP14Parser.NewtypeidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_newtypeid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            self.typespecifierseq()
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 750
                self.newdeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ptroperator(self):
            return self.getTypedRuleContext(CPP14Parser.PtroperatorContext,0)


        def newdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NewdeclaratorContext,0)


        def noptrnewdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrnewdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_newdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewdeclarator" ):
                listener.enterNewdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewdeclarator" ):
                listener.exitNewdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewdeclarator" ):
                return visitor.visitNewdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def newdeclarator(self):

        localctx = CPP14Parser.NewdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_newdeclarator)
        try:
            self.state = 758
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Decltype, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.AndAnd, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 753
                self.ptroperator()
                self.state = 755
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 754
                    self.newdeclarator()


                pass
            elif token in [CPP14Parser.LeftBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 757
                self.noptrnewdeclarator(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoptrnewdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def noptrnewdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrnewdeclaratorContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_noptrnewdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoptrnewdeclarator" ):
                listener.enterNoptrnewdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoptrnewdeclarator" ):
                listener.exitNoptrnewdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoptrnewdeclarator" ):
                return visitor.visitNoptrnewdeclarator(self)
            else:
                return visitor.visitChildren(self)



    def noptrnewdeclarator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.NoptrnewdeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_noptrnewdeclarator, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
            self.match(CPP14Parser.LeftBracket)
            self.state = 762
            self.expression(0)
            self.state = 763
            self.match(CPP14Parser.RightBracket)
            self.state = 765
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 764
                self.attributespecifierseq(0)


            self._ctx.stop = self._input.LT(-1)
            self.state = 776
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.NoptrnewdeclaratorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrnewdeclarator)
                    self.state = 767
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 768
                    self.match(CPP14Parser.LeftBracket)
                    self.state = 769
                    self.constantexpression()
                    self.state = 770
                    self.match(CPP14Parser.RightBracket)
                    self.state = 772
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 771
                        self.attributespecifierseq(0)

             
                self.state = 778
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NewinitializerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionlist(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionlistContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_newinitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewinitializer" ):
                listener.enterNewinitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewinitializer" ):
                listener.exitNewinitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewinitializer" ):
                return visitor.visitNewinitializer(self)
            else:
                return visitor.visitChildren(self)




    def newinitializer(self):

        localctx = CPP14Parser.NewinitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_newinitializer)
        self._la = 0 # Token type
        try:
            self.state = 785
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.LeftParen]:
                self.enterOuterAlt(localctx, 1)
                self.state = 779
                self.match(CPP14Parser.LeftParen)
                self.state = 781
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 780
                    self.expressionlist()


                self.state = 783
                self.match(CPP14Parser.RightParen)
                pass
            elif token in [CPP14Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 784
                self.bracedinitlist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeleteexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Delete(self):
            return self.getToken(CPP14Parser.Delete, 0)

        def castexpression(self):
            return self.getTypedRuleContext(CPP14Parser.CastexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_deleteexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteexpression" ):
                listener.enterDeleteexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteexpression" ):
                listener.exitDeleteexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteexpression" ):
                return visitor.visitDeleteexpression(self)
            else:
                return visitor.visitChildren(self)




    def deleteexpression(self):

        localctx = CPP14Parser.DeleteexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_deleteexpression)
        self._la = 0 # Token type
        try:
            self.state = 799
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 788
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Doublecolon:
                    self.state = 787
                    self.match(CPP14Parser.Doublecolon)


                self.state = 790
                self.match(CPP14Parser.Delete)
                self.state = 791
                self.castexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 793
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Doublecolon:
                    self.state = 792
                    self.match(CPP14Parser.Doublecolon)


                self.state = 795
                self.match(CPP14Parser.Delete)
                self.state = 796
                self.match(CPP14Parser.LeftBracket)
                self.state = 797
                self.match(CPP14Parser.RightBracket)
                self.state = 798
                self.castexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoexceptexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Noexcept(self):
            return self.getToken(CPP14Parser.Noexcept, 0)

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_noexceptexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoexceptexpression" ):
                listener.enterNoexceptexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoexceptexpression" ):
                listener.exitNoexceptexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoexceptexpression" ):
                return visitor.visitNoexceptexpression(self)
            else:
                return visitor.visitChildren(self)




    def noexceptexpression(self):

        localctx = CPP14Parser.NoexceptexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_noexceptexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 801
            self.match(CPP14Parser.Noexcept)
            self.state = 802
            self.match(CPP14Parser.LeftParen)
            self.state = 803
            self.expression(0)
            self.state = 804
            self.match(CPP14Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CastexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryexpression(self):
            return self.getTypedRuleContext(CPP14Parser.UnaryexpressionContext,0)


        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def castexpression(self):
            return self.getTypedRuleContext(CPP14Parser.CastexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_castexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastexpression" ):
                listener.enterCastexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastexpression" ):
                listener.exitCastexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastexpression" ):
                return visitor.visitCastexpression(self)
            else:
                return visitor.visitChildren(self)




    def castexpression(self):

        localctx = CPP14Parser.CastexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_castexpression)
        try:
            self.state = 812
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 806
                self.unaryexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 807
                self.match(CPP14Parser.LeftParen)
                self.state = 808
                self.typeid()
                self.state = 809
                self.match(CPP14Parser.RightParen)
                self.state = 810
                self.castexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PmexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def castexpression(self):
            return self.getTypedRuleContext(CPP14Parser.CastexpressionContext,0)


        def pmexpression(self):
            return self.getTypedRuleContext(CPP14Parser.PmexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_pmexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPmexpression" ):
                listener.enterPmexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPmexpression" ):
                listener.exitPmexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPmexpression" ):
                return visitor.visitPmexpression(self)
            else:
                return visitor.visitChildren(self)



    def pmexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.PmexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_pmexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.castexpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 825
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 823
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.PmexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pmexpression)
                        self.state = 817
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 818
                        self.match(CPP14Parser.DotStar)
                        self.state = 819
                        self.castexpression()
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.PmexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_pmexpression)
                        self.state = 820
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 821
                        self.match(CPP14Parser.ArrowStar)
                        self.state = 822
                        self.castexpression()
                        pass

             
                self.state = 827
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MultiplicativeexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pmexpression(self):
            return self.getTypedRuleContext(CPP14Parser.PmexpressionContext,0)


        def multiplicativeexpression(self):
            return self.getTypedRuleContext(CPP14Parser.MultiplicativeexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_multiplicativeexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeexpression" ):
                listener.enterMultiplicativeexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeexpression" ):
                listener.exitMultiplicativeexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeexpression" ):
                return visitor.visitMultiplicativeexpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.MultiplicativeexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_multiplicativeexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.pmexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 842
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 840
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.MultiplicativeexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeexpression)
                        self.state = 831
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 832
                        self.match(CPP14Parser.Star)
                        self.state = 833
                        self.pmexpression(0)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.MultiplicativeexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeexpression)
                        self.state = 834
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 835
                        self.match(CPP14Parser.Div)
                        self.state = 836
                        self.pmexpression(0)
                        pass

                    elif la_ == 3:
                        localctx = CPP14Parser.MultiplicativeexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeexpression)
                        self.state = 837
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 838
                        self.match(CPP14Parser.Mod)
                        self.state = 839
                        self.pmexpression(0)
                        pass

             
                self.state = 844
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AdditiveexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeexpression(self):
            return self.getTypedRuleContext(CPP14Parser.MultiplicativeexpressionContext,0)


        def additiveexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AdditiveexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_additiveexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveexpression" ):
                listener.enterAdditiveexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveexpression" ):
                listener.exitAdditiveexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveexpression" ):
                return visitor.visitAdditiveexpression(self)
            else:
                return visitor.visitChildren(self)



    def additiveexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.AdditiveexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_additiveexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 846
            self.multiplicativeexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 856
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 854
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.AdditiveexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveexpression)
                        self.state = 848
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 849
                        self.match(CPP14Parser.Plus)
                        self.state = 850
                        self.multiplicativeexpression(0)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.AdditiveexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveexpression)
                        self.state = 851
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 852
                        self.match(CPP14Parser.Minus)
                        self.state = 853
                        self.multiplicativeexpression(0)
                        pass

             
                self.state = 858
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ShiftexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AdditiveexpressionContext,0)


        def shiftexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ShiftexpressionContext,0)


        def rightShift(self):
            return self.getTypedRuleContext(CPP14Parser.RightShiftContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_shiftexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftexpression" ):
                listener.enterShiftexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftexpression" ):
                listener.exitShiftexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftexpression" ):
                return visitor.visitShiftexpression(self)
            else:
                return visitor.visitChildren(self)



    def shiftexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.ShiftexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_shiftexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 860
            self.additiveexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 871
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 869
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.ShiftexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftexpression)
                        self.state = 862
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 863
                        self.match(CPP14Parser.LeftShift)
                        self.state = 864
                        self.additiveexpression(0)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.ShiftexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftexpression)
                        self.state = 865
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 866
                        self.rightShift()
                        self.state = 867
                        self.additiveexpression(0)
                        pass

             
                self.state = 873
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RelationalexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ShiftexpressionContext,0)


        def relationalexpression(self):
            return self.getTypedRuleContext(CPP14Parser.RelationalexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_relationalexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalexpression" ):
                listener.enterRelationalexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalexpression" ):
                listener.exitRelationalexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalexpression" ):
                return visitor.visitRelationalexpression(self)
            else:
                return visitor.visitChildren(self)



    def relationalexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.RelationalexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_relationalexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 875
            self.shiftexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 891
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 889
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.RelationalexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalexpression)
                        self.state = 877
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 878
                        self.match(CPP14Parser.Less)
                        self.state = 879
                        self.shiftexpression(0)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.RelationalexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalexpression)
                        self.state = 880
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 881
                        self.match(CPP14Parser.Greater)
                        self.state = 882
                        self.shiftexpression(0)
                        pass

                    elif la_ == 3:
                        localctx = CPP14Parser.RelationalexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalexpression)
                        self.state = 883
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 884
                        self.match(CPP14Parser.LessEqual)
                        self.state = 885
                        self.shiftexpression(0)
                        pass

                    elif la_ == 4:
                        localctx = CPP14Parser.RelationalexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalexpression)
                        self.state = 886
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 887
                        self.match(CPP14Parser.GreaterEqual)
                        self.state = 888
                        self.shiftexpression(0)
                        pass

             
                self.state = 893
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class EqualityexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalexpression(self):
            return self.getTypedRuleContext(CPP14Parser.RelationalexpressionContext,0)


        def equalityexpression(self):
            return self.getTypedRuleContext(CPP14Parser.EqualityexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_equalityexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityexpression" ):
                listener.enterEqualityexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityexpression" ):
                listener.exitEqualityexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityexpression" ):
                return visitor.visitEqualityexpression(self)
            else:
                return visitor.visitChildren(self)



    def equalityexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.EqualityexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_equalityexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 895
            self.relationalexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 905
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 903
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.EqualityexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityexpression)
                        self.state = 897
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 898
                        self.match(CPP14Parser.Equal)
                        self.state = 899
                        self.relationalexpression(0)
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.EqualityexpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityexpression)
                        self.state = 900
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 901
                        self.match(CPP14Parser.NotEqual)
                        self.state = 902
                        self.relationalexpression(0)
                        pass

             
                self.state = 907
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AndexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityexpression(self):
            return self.getTypedRuleContext(CPP14Parser.EqualityexpressionContext,0)


        def andexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AndexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_andexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndexpression" ):
                listener.enterAndexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndexpression" ):
                listener.exitAndexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndexpression" ):
                return visitor.visitAndexpression(self)
            else:
                return visitor.visitChildren(self)



    def andexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.AndexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_andexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 909
            self.equalityexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 916
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.AndexpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andexpression)
                    self.state = 911
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 912
                    self.match(CPP14Parser.And)
                    self.state = 913
                    self.equalityexpression(0) 
                self.state = 918
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExclusiveorexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AndexpressionContext,0)


        def exclusiveorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ExclusiveorexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_exclusiveorexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusiveorexpression" ):
                listener.enterExclusiveorexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusiveorexpression" ):
                listener.exitExclusiveorexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExclusiveorexpression" ):
                return visitor.visitExclusiveorexpression(self)
            else:
                return visitor.visitChildren(self)



    def exclusiveorexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.ExclusiveorexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exclusiveorexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 920
            self.andexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 927
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.ExclusiveorexpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exclusiveorexpression)
                    self.state = 922
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 923
                    self.match(CPP14Parser.Caret)
                    self.state = 924
                    self.andexpression(0) 
                self.state = 929
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class InclusiveorexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exclusiveorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ExclusiveorexpressionContext,0)


        def inclusiveorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.InclusiveorexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_inclusiveorexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusiveorexpression" ):
                listener.enterInclusiveorexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusiveorexpression" ):
                listener.exitInclusiveorexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclusiveorexpression" ):
                return visitor.visitInclusiveorexpression(self)
            else:
                return visitor.visitChildren(self)



    def inclusiveorexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.InclusiveorexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_inclusiveorexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 931
            self.exclusiveorexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 938
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.InclusiveorexpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_inclusiveorexpression)
                    self.state = 933
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 934
                    self.match(CPP14Parser.Or)
                    self.state = 935
                    self.exclusiveorexpression(0) 
                self.state = 940
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LogicalandexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inclusiveorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.InclusiveorexpressionContext,0)


        def logicalandexpression(self):
            return self.getTypedRuleContext(CPP14Parser.LogicalandexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_logicalandexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalandexpression" ):
                listener.enterLogicalandexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalandexpression" ):
                listener.exitLogicalandexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalandexpression" ):
                return visitor.visitLogicalandexpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalandexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.LogicalandexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_logicalandexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 942
            self.inclusiveorexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 949
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.LogicalandexpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalandexpression)
                    self.state = 944
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 945
                    self.match(CPP14Parser.AndAnd)
                    self.state = 946
                    self.inclusiveorexpression(0) 
                self.state = 951
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LogicalorexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalandexpression(self):
            return self.getTypedRuleContext(CPP14Parser.LogicalandexpressionContext,0)


        def logicalorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.LogicalorexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_logicalorexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalorexpression" ):
                listener.enterLogicalorexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalorexpression" ):
                listener.exitLogicalorexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalorexpression" ):
                return visitor.visitLogicalorexpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalorexpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.LogicalorexpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_logicalorexpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 953
            self.logicalandexpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 960
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.LogicalorexpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalorexpression)
                    self.state = 955
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 956
                    self.match(CPP14Parser.OrOr)
                    self.state = 957
                    self.logicalandexpression(0) 
                self.state = 962
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConditionalexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.LogicalorexpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_conditionalexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalexpression" ):
                listener.enterConditionalexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalexpression" ):
                listener.exitConditionalexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalexpression" ):
                return visitor.visitConditionalexpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalexpression(self):

        localctx = CPP14Parser.ConditionalexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_conditionalexpression)
        try:
            self.state = 970
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 963
                self.logicalorexpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 964
                self.logicalorexpression(0)
                self.state = 965
                self.match(CPP14Parser.Question)
                self.state = 966
                self.expression(0)
                self.state = 967
                self.match(CPP14Parser.Colon)
                self.state = 968
                self.assignmentexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConditionalexpressionContext,0)


        def logicalorexpression(self):
            return self.getTypedRuleContext(CPP14Parser.LogicalorexpressionContext,0)


        def assignmentoperator(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentoperatorContext,0)


        def initializerclause(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerclauseContext,0)


        def throwexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ThrowexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_assignmentexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentexpression" ):
                listener.enterAssignmentexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentexpression" ):
                listener.exitAssignmentexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentexpression" ):
                return visitor.visitAssignmentexpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentexpression(self):

        localctx = CPP14Parser.AssignmentexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignmentexpression)
        try:
            self.state = 978
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 972
                self.conditionalexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 973
                self.logicalorexpression(0)
                self.state = 974
                self.assignmentoperator()
                self.state = 975
                self.initializerclause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 977
                self.throwexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Co_assignmentexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentexpressionContext,0)


        def yieldexpression(self):
            return self.getTypedRuleContext(CPP14Parser.YieldexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_assignmentexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_assignmentexpression" ):
                listener.enterCo_assignmentexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_assignmentexpression" ):
                listener.exitCo_assignmentexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_assignmentexpression" ):
                return visitor.visitCo_assignmentexpression(self)
            else:
                return visitor.visitChildren(self)




    def co_assignmentexpression(self):

        localctx = CPP14Parser.Co_assignmentexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_co_assignmentexpression)
        try:
            self.state = 982
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Alignof, CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Const_cast, CPP14Parser.Decltype, CPP14Parser.Delete, CPP14Parser.Double, CPP14Parser.Dynamic_cast, CPP14Parser.KFalse, CPP14Parser.Float, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.New, CPP14Parser.Noexcept, CPP14Parser.Nullptr, CPP14Parser.Operator, CPP14Parser.Reinterpret_cast, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Sizeof, CPP14Parser.Static_cast, CPP14Parser.This, CPP14Parser.Throw, CPP14Parser.KTrue, CPP14Parser.Typeid, CPP14Parser.Typename, CPP14Parser.Unsigned, CPP14Parser.Void, CPP14Parser.Wchar, CPP14Parser.LeftParen, CPP14Parser.LeftBracket, CPP14Parser.Plus, CPP14Parser.Minus, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.Or, CPP14Parser.Tilde, CPP14Parser.Not, CPP14Parser.PlusPlus, CPP14Parser.MinusMinus, CPP14Parser.Doublecolon, CPP14Parser.Identifier, CPP14Parser.Integerliteral, CPP14Parser.Characterliteral, CPP14Parser.Floatingliteral, CPP14Parser.Stringliteral, CPP14Parser.Userdefinedintegerliteral, CPP14Parser.Userdefinedfloatingliteral, CPP14Parser.Userdefinedstringliteral, CPP14Parser.Userdefinedcharacterliteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 980
                self.assignmentexpression()
                pass
            elif token in [CPP14Parser.CoYield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 981
                self.yieldexpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class YieldexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CoYield(self):
            return self.getToken(CPP14Parser.CoYield, 0)

        def assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentexpressionContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)

        def getText(self):
            return 'CO_YIELD(%s)' % self.getDirtyText([1])

        def getRuleIndex(self):
            return CPP14Parser.RULE_yieldexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYieldexpression" ):
                listener.enterYieldexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYieldexpression" ):
                listener.exitYieldexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYieldexpression" ):
                return visitor.visitYieldexpression(self)
            else:
                return visitor.visitChildren(self)




    def yieldexpression(self):

        localctx = CPP14Parser.YieldexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_yieldexpression)
        try:
            self.state = 988
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 984
                self.match(CPP14Parser.CoYield)
                self.state = 985
                self.assignmentexpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 986
                self.match(CPP14Parser.CoYield)
                self.state = 987
                self.bracedinitlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentoperatorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rightShiftAssign(self):
            return self.getTypedRuleContext(CPP14Parser.RightShiftAssignContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_assignmentoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentoperator" ):
                listener.enterAssignmentoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentoperator" ):
                listener.exitAssignmentoperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentoperator" ):
                return visitor.visitAssignmentoperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentoperator(self):

        localctx = CPP14Parser.AssignmentoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_assignmentoperator)
        try:
            self.state = 1001
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Assign]:
                self.enterOuterAlt(localctx, 1)
                self.state = 990
                self.match(CPP14Parser.Assign)
                pass
            elif token in [CPP14Parser.StarAssign]:
                self.enterOuterAlt(localctx, 2)
                self.state = 991
                self.match(CPP14Parser.StarAssign)
                pass
            elif token in [CPP14Parser.DivAssign]:
                self.enterOuterAlt(localctx, 3)
                self.state = 992
                self.match(CPP14Parser.DivAssign)
                pass
            elif token in [CPP14Parser.ModAssign]:
                self.enterOuterAlt(localctx, 4)
                self.state = 993
                self.match(CPP14Parser.ModAssign)
                pass
            elif token in [CPP14Parser.PlusAssign]:
                self.enterOuterAlt(localctx, 5)
                self.state = 994
                self.match(CPP14Parser.PlusAssign)
                pass
            elif token in [CPP14Parser.MinusAssign]:
                self.enterOuterAlt(localctx, 6)
                self.state = 995
                self.match(CPP14Parser.MinusAssign)
                pass
            elif token in [CPP14Parser.Greater]:
                self.enterOuterAlt(localctx, 7)
                self.state = 996
                self.rightShiftAssign()
                pass
            elif token in [CPP14Parser.LeftShiftAssign]:
                self.enterOuterAlt(localctx, 8)
                self.state = 997
                self.match(CPP14Parser.LeftShiftAssign)
                pass
            elif token in [CPP14Parser.AndAssign]:
                self.enterOuterAlt(localctx, 9)
                self.state = 998
                self.match(CPP14Parser.AndAssign)
                pass
            elif token in [CPP14Parser.XorAssign]:
                self.enterOuterAlt(localctx, 10)
                self.state = 999
                self.match(CPP14Parser.XorAssign)
                pass
            elif token in [CPP14Parser.OrAssign]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1000
                self.match(CPP14Parser.OrAssign)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentexpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1004
            self.assignmentexpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1011
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 1006
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1007
                    self.match(CPP14Parser.Comma)
                    self.state = 1008
                    self.assignmentexpression() 
                self.state = 1013
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Co_expressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def co_assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.Co_assignmentexpressionContext,0)


        def co_expression(self):
            return self.getTypedRuleContext(CPP14Parser.Co_expressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_expression" ):
                listener.enterCo_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_expression" ):
                listener.exitCo_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_expression" ):
                return visitor.visitCo_expression(self)
            else:
                return visitor.visitChildren(self)



    def co_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.Co_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_co_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1015
            self.co_assignmentexpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1022
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.Co_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_co_expression)
                    self.state = 1017
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1018
                    self.match(CPP14Parser.Comma)
                    self.state = 1019
                    self.co_assignmentexpression() 
                self.state = 1024
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConstantexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConditionalexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_constantexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantexpression" ):
                listener.enterConstantexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantexpression" ):
                listener.exitConstantexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantexpression" ):
                return visitor.visitConstantexpression(self)
            else:
                return visitor.visitChildren(self)




    def constantexpression(self):

        localctx = CPP14Parser.ConstantexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_constantexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            self.conditionalexpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeledstatement(self):
            return self.getTypedRuleContext(CPP14Parser.LabeledstatementContext,0)


        def expressionstatement(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionstatementContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.CompoundstatementContext,0)


        def selectionstatement(self):
            return self.getTypedRuleContext(CPP14Parser.SelectionstatementContext,0)


        def iterationstatement(self):
            return self.getTypedRuleContext(CPP14Parser.IterationstatementContext,0)


        def jumpstatement(self):
            return self.getTypedRuleContext(CPP14Parser.JumpstatementContext,0)


        def declarationstatement(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationstatementContext,0)


        def tryblock(self):
            return self.getTypedRuleContext(CPP14Parser.TryblockContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CPP14Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 1053
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1027
                self.labeledstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1029
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1028
                    self.attributespecifierseq(0)


                self.state = 1031
                self.expressionstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1033
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1032
                    self.attributespecifierseq(0)


                self.state = 1035
                self.compoundstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1037
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1036
                    self.attributespecifierseq(0)


                self.state = 1039
                self.selectionstatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1041
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1040
                    self.attributespecifierseq(0)


                self.state = 1043
                self.iterationstatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1045
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1044
                    self.attributespecifierseq(0)


                self.state = 1047
                self.jumpstatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1048
                self.declarationstatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1050
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1049
                    self.attributespecifierseq(0)


                self.state = 1052
                self.tryblock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Co_statementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CPP14Parser.StatementContext,0)


        def co_expressionstatement(self):
            return self.getTypedRuleContext(CPP14Parser.Co_expressionstatementContext,0)


        def co_jumpstatement(self):
            return self.getTypedRuleContext(CPP14Parser.Co_jumpstatementContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_statement" ):
                listener.enterCo_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_statement" ):
                listener.exitCo_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_statement" ):
                return visitor.visitCo_statement(self)
            else:
                return visitor.visitChildren(self)




    def co_statement(self):

        localctx = CPP14Parser.Co_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_co_statement)
        try:
            self.state = 1058
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1055
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1056
                self.co_expressionstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1057
                self.co_jumpstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabeledstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def statement(self):
            return self.getTypedRuleContext(CPP14Parser.StatementContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def Case(self):
            return self.getToken(CPP14Parser.Case, 0)

        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def Default(self):
            return self.getToken(CPP14Parser.Default, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_labeledstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledstatement" ):
                listener.enterLabeledstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledstatement" ):
                listener.exitLabeledstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledstatement" ):
                return visitor.visitLabeledstatement(self)
            else:
                return visitor.visitChildren(self)




    def labeledstatement(self):

        localctx = CPP14Parser.LabeledstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_labeledstatement)
        self._la = 0 # Token type
        try:
            self.state = 1080
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1061
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1060
                    self.attributespecifierseq(0)


                self.state = 1063
                self.match(CPP14Parser.Identifier)
                self.state = 1064
                self.match(CPP14Parser.Colon)
                self.state = 1065
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1067
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1066
                    self.attributespecifierseq(0)


                self.state = 1069
                self.match(CPP14Parser.Case)
                self.state = 1070
                self.constantexpression()
                self.state = 1071
                self.match(CPP14Parser.Colon)
                self.state = 1072
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1075
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1074
                    self.attributespecifierseq(0)


                self.state = 1077
                self.match(CPP14Parser.Default)
                self.state = 1078
                self.match(CPP14Parser.Colon)
                self.state = 1079
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_expressionstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionstatement" ):
                listener.enterExpressionstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionstatement" ):
                listener.exitExpressionstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionstatement" ):
                return visitor.visitExpressionstatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionstatement(self):

        localctx = CPP14Parser.ExpressionstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expressionstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1083
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                self.state = 1082
                self.expression(0)


            self.state = 1085
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Co_expressionstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def co_expression(self):
            return self.getTypedRuleContext(CPP14Parser.Co_expressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_expressionstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_expressionstatement" ):
                listener.enterCo_expressionstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_expressionstatement" ):
                listener.exitCo_expressionstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_expressionstatement" ):
                return visitor.visitCo_expressionstatement(self)
            else:
                return visitor.visitChildren(self)




    def co_expressionstatement(self):

        localctx = CPP14Parser.Co_expressionstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_co_expressionstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1088
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.CoYield) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                self.state = 1087
                self.co_expression(0)


            self.state = 1090
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementseq(self):
            return self.getTypedRuleContext(CPP14Parser.StatementseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_compoundstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundstatement" ):
                listener.enterCompoundstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundstatement" ):
                listener.exitCompoundstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundstatement" ):
                return visitor.visitCompoundstatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundstatement(self):

        localctx = CPP14Parser.CompoundstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_compoundstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1092
            self.match(CPP14Parser.LeftBrace)
            self.state = 1094
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Asm) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Break) | (1 << CPP14Parser.Case) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Continue) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Default) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Do) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.For) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Goto) | (1 << CPP14Parser.If) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Namespace) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Return) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Static_cast) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Switch))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Thread_local - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Try - 64)) | (1 << (CPP14Parser.Typedef - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Union - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Using - 64)) | (1 << (CPP14Parser.Virtual - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Volatile - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.While - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.AndAnd - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Semi - 64)) | (1 << (CPP14Parser.Ellipsis - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                self.state = 1093
                self.statementseq(0)


            self.state = 1096
            self.match(CPP14Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Co_compoundstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def co_statementseq(self):
            return self.getTypedRuleContext(CPP14Parser.Co_statementseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_compoundstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_compoundstatement" ):
                listener.enterCo_compoundstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_compoundstatement" ):
                listener.exitCo_compoundstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_compoundstatement" ):
                return visitor.visitCo_compoundstatement(self)
            else:
                return visitor.visitChildren(self)




    def co_compoundstatement(self):

        localctx = CPP14Parser.Co_compoundstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_co_compoundstatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1098
            self.match(CPP14Parser.LeftBrace)
            self.state = 1100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Asm) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Break) | (1 << CPP14Parser.Case) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Continue) | (1 << CPP14Parser.CoReturn) | (1 << CPP14Parser.CoYield) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Default) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Do) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.For) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Goto) | (1 << CPP14Parser.If) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Namespace) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Return) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Static_cast) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Switch))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Thread_local - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Try - 64)) | (1 << (CPP14Parser.Typedef - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Union - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Using - 64)) | (1 << (CPP14Parser.Virtual - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Volatile - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.While - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.AndAnd - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Semi - 64)) | (1 << (CPP14Parser.Ellipsis - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                self.state = 1099
                self.co_statementseq(0)


            self.state = 1102
            self.match(CPP14Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CPP14Parser.StatementContext,0)


        def statementseq(self):
            return self.getTypedRuleContext(CPP14Parser.StatementseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_statementseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementseq" ):
                listener.enterStatementseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementseq" ):
                listener.exitStatementseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementseq" ):
                return visitor.visitStatementseq(self)
            else:
                return visitor.visitChildren(self)



    def statementseq(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.StatementseqContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_statementseq, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1105
            self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.StatementseqContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statementseq)
                    self.state = 1107
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1108
                    self.statement() 
                self.state = 1113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Co_statementseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def co_statement(self):
            return self.getTypedRuleContext(CPP14Parser.Co_statementContext,0)


        def co_statementseq(self):
            return self.getTypedRuleContext(CPP14Parser.Co_statementseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_statementseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_statementseq" ):
                listener.enterCo_statementseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_statementseq" ):
                listener.exitCo_statementseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_statementseq" ):
                return visitor.visitCo_statementseq(self)
            else:
                return visitor.visitChildren(self)



    def co_statementseq(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.Co_statementseqContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_co_statementseq, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1115
            self.co_statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,94,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.Co_statementseqContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_co_statementseq)
                    self.state = 1117
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1118
                    self.co_statement() 
                self.state = 1123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SelectionstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(CPP14Parser.If, 0)

        def condition(self):
            return self.getTypedRuleContext(CPP14Parser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPP14Parser.StatementContext)
            else:
                return self.getTypedRuleContext(CPP14Parser.StatementContext,i)


        def Else(self):
            return self.getToken(CPP14Parser.Else, 0)

        def Switch(self):
            return self.getToken(CPP14Parser.Switch, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_selectionstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionstatement" ):
                listener.enterSelectionstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionstatement" ):
                listener.exitSelectionstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectionstatement" ):
                return visitor.visitSelectionstatement(self)
            else:
                return visitor.visitChildren(self)




    def selectionstatement(self):

        localctx = CPP14Parser.SelectionstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_selectionstatement)
        try:
            self.state = 1144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1124
                self.match(CPP14Parser.If)
                self.state = 1125
                self.match(CPP14Parser.LeftParen)
                self.state = 1126
                self.condition()
                self.state = 1127
                self.match(CPP14Parser.RightParen)
                self.state = 1128
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1130
                self.match(CPP14Parser.If)
                self.state = 1131
                self.match(CPP14Parser.LeftParen)
                self.state = 1132
                self.condition()
                self.state = 1133
                self.match(CPP14Parser.RightParen)
                self.state = 1134
                self.statement()
                self.state = 1135
                self.match(CPP14Parser.Else)
                self.state = 1136
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1138
                self.match(CPP14Parser.Switch)
                self.state = 1139
                self.match(CPP14Parser.LeftParen)
                self.state = 1140
                self.condition()
                self.state = 1141
                self.match(CPP14Parser.RightParen)
                self.state = 1142
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def initializerclause(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerclauseContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = CPP14Parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 1162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1146
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1147
                    self.attributespecifierseq(0)


                self.state = 1150
                self.declspecifierseq()
                self.state = 1151
                self.declarator()
                self.state = 1152
                self.match(CPP14Parser.Assign)
                self.state = 1153
                self.initializerclause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1155
                    self.attributespecifierseq(0)


                self.state = 1158
                self.declspecifierseq()
                self.state = 1159
                self.declarator()
                self.state = 1160
                self.bracedinitlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(CPP14Parser.While, 0)

        def condition(self):
            return self.getTypedRuleContext(CPP14Parser.ConditionContext,0)


        def statement(self):
            return self.getTypedRuleContext(CPP14Parser.StatementContext,0)


        def Do(self):
            return self.getToken(CPP14Parser.Do, 0)

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def For(self):
            return self.getToken(CPP14Parser.For, 0)

        def forinitstatement(self):
            return self.getTypedRuleContext(CPP14Parser.ForinitstatementContext,0)


        def forrangedeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.ForrangedeclarationContext,0)


        def forrangeinitializer(self):
            return self.getTypedRuleContext(CPP14Parser.ForrangeinitializerContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_iterationstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterationstatement" ):
                listener.enterIterationstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterationstatement" ):
                listener.exitIterationstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterationstatement" ):
                return visitor.visitIterationstatement(self)
            else:
                return visitor.visitChildren(self)




    def iterationstatement(self):

        localctx = CPP14Parser.IterationstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_iterationstatement)
        self._la = 0 # Token type
        try:
            self.state = 1199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,101,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1164
                self.match(CPP14Parser.While)
                self.state = 1165
                self.match(CPP14Parser.LeftParen)
                self.state = 1166
                self.condition()
                self.state = 1167
                self.match(CPP14Parser.RightParen)
                self.state = 1168
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1170
                self.match(CPP14Parser.Do)
                self.state = 1171
                self.statement()
                self.state = 1172
                self.match(CPP14Parser.While)
                self.state = 1173
                self.match(CPP14Parser.LeftParen)
                self.state = 1174
                self.expression(0)
                self.state = 1175
                self.match(CPP14Parser.RightParen)
                self.state = 1176
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1178
                self.match(CPP14Parser.For)
                self.state = 1179
                self.match(CPP14Parser.LeftParen)
                self.state = 1180
                self.forinitstatement()
                self.state = 1182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_cast) | (1 << CPP14Parser.Struct))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Thread_local - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typedef - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Union - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Virtual - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Volatile - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 1181
                    self.condition()


                self.state = 1184
                self.match(CPP14Parser.Semi)
                self.state = 1186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 1185
                    self.expression(0)


                self.state = 1188
                self.match(CPP14Parser.RightParen)
                self.state = 1189
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1191
                self.match(CPP14Parser.For)
                self.state = 1192
                self.match(CPP14Parser.LeftParen)
                self.state = 1193
                self.forrangedeclaration()
                self.state = 1194
                self.match(CPP14Parser.Colon)
                self.state = 1195
                self.forrangeinitializer()
                self.state = 1196
                self.match(CPP14Parser.RightParen)
                self.state = 1197
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForinitstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionstatement(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionstatementContext,0)


        def simpledeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.SimpledeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_forinitstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForinitstatement" ):
                listener.enterForinitstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForinitstatement" ):
                listener.exitForinitstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinitstatement" ):
                return visitor.visitForinitstatement(self)
            else:
                return visitor.visitChildren(self)




    def forinitstatement(self):

        localctx = CPP14Parser.ForinitstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_forinitstatement)
        try:
            self.state = 1203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1201
                self.expressionstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1202
                self.simpledeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForrangedeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_forrangedeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForrangedeclaration" ):
                listener.enterForrangedeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForrangedeclaration" ):
                listener.exitForrangedeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForrangedeclaration" ):
                return visitor.visitForrangedeclaration(self)
            else:
                return visitor.visitChildren(self)




    def forrangedeclaration(self):

        localctx = CPP14Parser.ForrangedeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_forrangedeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 1205
                self.attributespecifierseq(0)


            self.state = 1208
            self.declspecifierseq()
            self.state = 1209
            self.declarator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForrangeinitializerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_forrangeinitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForrangeinitializer" ):
                listener.enterForrangeinitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForrangeinitializer" ):
                listener.exitForrangeinitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForrangeinitializer" ):
                return visitor.visitForrangeinitializer(self)
            else:
                return visitor.visitChildren(self)




    def forrangeinitializer(self):

        localctx = CPP14Parser.ForrangeinitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_forrangeinitializer)
        try:
            self.state = 1213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Alignof, CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Const_cast, CPP14Parser.Decltype, CPP14Parser.Delete, CPP14Parser.Double, CPP14Parser.Dynamic_cast, CPP14Parser.KFalse, CPP14Parser.Float, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.New, CPP14Parser.Noexcept, CPP14Parser.Nullptr, CPP14Parser.Operator, CPP14Parser.Reinterpret_cast, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Sizeof, CPP14Parser.Static_cast, CPP14Parser.This, CPP14Parser.Throw, CPP14Parser.KTrue, CPP14Parser.Typeid, CPP14Parser.Typename, CPP14Parser.Unsigned, CPP14Parser.Void, CPP14Parser.Wchar, CPP14Parser.LeftParen, CPP14Parser.LeftBracket, CPP14Parser.Plus, CPP14Parser.Minus, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.Or, CPP14Parser.Tilde, CPP14Parser.Not, CPP14Parser.PlusPlus, CPP14Parser.MinusMinus, CPP14Parser.Doublecolon, CPP14Parser.Identifier, CPP14Parser.Integerliteral, CPP14Parser.Characterliteral, CPP14Parser.Floatingliteral, CPP14Parser.Stringliteral, CPP14Parser.Userdefinedintegerliteral, CPP14Parser.Userdefinedfloatingliteral, CPP14Parser.Userdefinedstringliteral, CPP14Parser.Userdefinedcharacterliteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1211
                self.expression(0)
                pass
            elif token in [CPP14Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1212
                self.bracedinitlist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JumpstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(CPP14Parser.Break, 0)

        def Continue(self):
            return self.getToken(CPP14Parser.Continue, 0)

        def Return(self):
            return self.getToken(CPP14Parser.Return, 0)

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def Goto(self):
            return self.getToken(CPP14Parser.Goto, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_jumpstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpstatement" ):
                listener.enterJumpstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpstatement" ):
                listener.exitJumpstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpstatement" ):
                return visitor.visitJumpstatement(self)
            else:
                return visitor.visitChildren(self)




    def jumpstatement(self):

        localctx = CPP14Parser.JumpstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_jumpstatement)
        self._la = 0 # Token type
        try:
            self.state = 1231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1215
                self.match(CPP14Parser.Break)
                self.state = 1216
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1217
                self.match(CPP14Parser.Continue)
                self.state = 1218
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1219
                self.match(CPP14Parser.Return)
                self.state = 1221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 1220
                    self.expression(0)


                self.state = 1223
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1224
                self.match(CPP14Parser.Return)
                self.state = 1225
                self.bracedinitlist()
                self.state = 1226
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1228
                self.match(CPP14Parser.Goto)
                self.state = 1229
                self.match(CPP14Parser.Identifier)
                self.state = 1230
                self.match(CPP14Parser.Semi)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Co_jumpstatementContext(PrettyPrintParserRuleContext):
        def getText(self):
            return 'CO_RETURN(%s)' % self.getDirtyText([1])

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CoReturn(self):
            return self.getToken(CPP14Parser.CoReturn, 0)

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def jumpstatement(self):
            return self.getTypedRuleContext(CPP14Parser.JumpstatementContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_co_jumpstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCo_jumpstatement" ):
                listener.enterCo_jumpstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCo_jumpstatement" ):
                listener.exitCo_jumpstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCo_jumpstatement" ):
                return visitor.visitCo_jumpstatement(self)
            else:
                return visitor.visitChildren(self)




    def co_jumpstatement(self):

        localctx = CPP14Parser.Co_jumpstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_co_jumpstatement)
        self._la = 0 # Token type
        try:
            self.state = 1243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1233
                self.match(CPP14Parser.CoReturn)
                self.state = 1235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 1234
                    self.expression(0)


                self.state = 1237
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1238
                self.match(CPP14Parser.CoReturn)
                self.state = 1239
                self.bracedinitlist()
                self.state = 1240
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1242
                self.jumpstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationstatementContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.BlockdeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_declarationstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationstatement" ):
                listener.enterDeclarationstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationstatement" ):
                listener.exitDeclarationstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationstatement" ):
                return visitor.visitDeclarationstatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationstatement(self):

        localctx = CPP14Parser.DeclarationstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_declarationstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1245
            self.blockdeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationContext,0)


        def declarationseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_declarationseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationseq" ):
                listener.enterDeclarationseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationseq" ):
                listener.exitDeclarationseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationseq" ):
                return visitor.visitDeclarationseq(self)
            else:
                return visitor.visitChildren(self)



    def declarationseq(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.DeclarationseqContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_declarationseq, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1248
            self.declaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,109,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.DeclarationseqContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationseq)
                    self.state = 1250
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1251
                    self.declaration() 
                self.state = 1256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.BlockdeclarationContext,0)


        def functiondefinition(self):
            return self.getTypedRuleContext(CPP14Parser.FunctiondefinitionContext,0)


        def coroutinedefinition(self):
            return self.getTypedRuleContext(CPP14Parser.CoroutinedefinitionContext,0)


        def templatedeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.TemplatedeclarationContext,0)


        def explicitinstantiation(self):
            return self.getTypedRuleContext(CPP14Parser.ExplicitinstantiationContext,0)


        def explicitspecialization(self):
            return self.getTypedRuleContext(CPP14Parser.ExplicitspecializationContext,0)


        def linkagespecification(self):
            return self.getTypedRuleContext(CPP14Parser.LinkagespecificationContext,0)


        def namespacedefinition(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacedefinitionContext,0)


        def emptydeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.EmptydeclarationContext,0)


        def attributedeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.AttributedeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CPP14Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_declaration)
        try:
            self.state = 1267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1257
                self.blockdeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1258
                self.functiondefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1259
                self.coroutinedefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1260
                self.templatedeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1261
                self.explicitinstantiation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1262
                self.explicitspecialization()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1263
                self.linkagespecification()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1264
                self.namespacedefinition()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1265
                self.emptydeclaration()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1266
                self.attributedeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpledeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.SimpledeclarationContext,0)


        def asmdefinition(self):
            return self.getTypedRuleContext(CPP14Parser.AsmdefinitionContext,0)


        def namespacealiasdefinition(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacealiasdefinitionContext,0)


        def usingdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.UsingdeclarationContext,0)


        def usingdirective(self):
            return self.getTypedRuleContext(CPP14Parser.UsingdirectiveContext,0)


        def static_assertdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.Static_assertdeclarationContext,0)


        def aliasdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.AliasdeclarationContext,0)


        def opaqueenumdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.OpaqueenumdeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_blockdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockdeclaration" ):
                listener.enterBlockdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockdeclaration" ):
                listener.exitBlockdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockdeclaration" ):
                return visitor.visitBlockdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def blockdeclaration(self):

        localctx = CPP14Parser.BlockdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_blockdeclaration)
        try:
            self.state = 1277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1269
                self.simpledeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1270
                self.asmdefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1271
                self.namespacealiasdefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1272
                self.usingdeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1273
                self.usingdirective()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1274
                self.static_assertdeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1275
                self.aliasdeclaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1276
                self.opaqueenumdeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AliasdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Using(self):
            return self.getToken(CPP14Parser.Using, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_aliasdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAliasdeclaration" ):
                listener.enterAliasdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAliasdeclaration" ):
                listener.exitAliasdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAliasdeclaration" ):
                return visitor.visitAliasdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def aliasdeclaration(self):

        localctx = CPP14Parser.AliasdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_aliasdeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1279
            self.match(CPP14Parser.Using)
            self.state = 1280
            self.match(CPP14Parser.Identifier)
            self.state = 1282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 1281
                self.attributespecifierseq(0)


            self.state = 1284
            self.match(CPP14Parser.Assign)
            self.state = 1285
            self.typeid()
            self.state = 1286
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpledeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def initdeclaratorlist(self):
            return self.getTypedRuleContext(CPP14Parser.InitdeclaratorlistContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_simpledeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpledeclaration" ):
                listener.enterSimpledeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpledeclaration" ):
                listener.exitSimpledeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpledeclaration" ):
                return visitor.visitSimpledeclaration(self)
            else:
                return visitor.visitChildren(self)




    def simpledeclaration(self):

        localctx = CPP14Parser.SimpledeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_simpledeclaration)
        self._la = 0 # Token type
        try:
            self.state = 1302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Class, CPP14Parser.Const, CPP14Parser.Constexpr, CPP14Parser.Decltype, CPP14Parser.Double, CPP14Parser.Enum, CPP14Parser.Explicit, CPP14Parser.Extern, CPP14Parser.Float, CPP14Parser.Friend, CPP14Parser.Inline, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.Mutable, CPP14Parser.Operator, CPP14Parser.Register, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Static, CPP14Parser.Struct, CPP14Parser.Thread_local, CPP14Parser.Typedef, CPP14Parser.Typename, CPP14Parser.Union, CPP14Parser.Unsigned, CPP14Parser.Virtual, CPP14Parser.Void, CPP14Parser.Volatile, CPP14Parser.Wchar, CPP14Parser.LeftParen, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.Tilde, CPP14Parser.AndAnd, CPP14Parser.Doublecolon, CPP14Parser.Semi, CPP14Parser.Ellipsis, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1289
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
                if la_ == 1:
                    self.state = 1288
                    self.declspecifierseq()


                self.state = 1292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Decltype or _la==CPP14Parser.Operator or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (CPP14Parser.LeftParen - 80)) | (1 << (CPP14Parser.Star - 80)) | (1 << (CPP14Parser.And - 80)) | (1 << (CPP14Parser.Tilde - 80)) | (1 << (CPP14Parser.AndAnd - 80)) | (1 << (CPP14Parser.Doublecolon - 80)) | (1 << (CPP14Parser.Ellipsis - 80)) | (1 << (CPP14Parser.Identifier - 80)))) != 0):
                    self.state = 1291
                    self.initdeclaratorlist(0)


                self.state = 1294
                self.match(CPP14Parser.Semi)
                pass
            elif token in [CPP14Parser.Alignas, CPP14Parser.LeftBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1295
                self.attributespecifierseq(0)
                self.state = 1297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
                if la_ == 1:
                    self.state = 1296
                    self.declspecifierseq()


                self.state = 1299
                self.initdeclaratorlist(0)
                self.state = 1300
                self.match(CPP14Parser.Semi)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Static_assertdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Static_assert(self):
            return self.getToken(CPP14Parser.Static_assert, 0)

        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def Stringliteral(self):
            return self.getToken(CPP14Parser.Stringliteral, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_static_assertdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_assertdeclaration" ):
                listener.enterStatic_assertdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_assertdeclaration" ):
                listener.exitStatic_assertdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_assertdeclaration" ):
                return visitor.visitStatic_assertdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def static_assertdeclaration(self):

        localctx = CPP14Parser.Static_assertdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_static_assertdeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1304
            self.match(CPP14Parser.Static_assert)
            self.state = 1305
            self.match(CPP14Parser.LeftParen)
            self.state = 1306
            self.constantexpression()
            self.state = 1307
            self.match(CPP14Parser.Comma)
            self.state = 1308
            self.match(CPP14Parser.Stringliteral)
            self.state = 1309
            self.match(CPP14Parser.RightParen)
            self.state = 1310
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptydeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPP14Parser.RULE_emptydeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptydeclaration" ):
                listener.enterEmptydeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptydeclaration" ):
                listener.exitEmptydeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptydeclaration" ):
                return visitor.visitEmptydeclaration(self)
            else:
                return visitor.visitChildren(self)




    def emptydeclaration(self):

        localctx = CPP14Parser.EmptydeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_emptydeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1312
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributedeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attributedeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributedeclaration" ):
                listener.enterAttributedeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributedeclaration" ):
                listener.exitAttributedeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedeclaration" ):
                return visitor.visitAttributedeclaration(self)
            else:
                return visitor.visitChildren(self)




    def attributedeclaration(self):

        localctx = CPP14Parser.AttributedeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_attributedeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1314
            self.attributespecifierseq(0)
            self.state = 1315
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def storageclassspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.StorageclassspecifierContext,0)


        def typespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierContext,0)


        def functionspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.FunctionspecifierContext,0)


        def Friend(self):
            return self.getToken(CPP14Parser.Friend, 0)

        def Typedef(self):
            return self.getToken(CPP14Parser.Typedef, 0)

        def Constexpr(self):
            return self.getToken(CPP14Parser.Constexpr, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_declspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclspecifier" ):
                listener.enterDeclspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclspecifier" ):
                listener.exitDeclspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclspecifier" ):
                return visitor.visitDeclspecifier(self)
            else:
                return visitor.visitChildren(self)




    def declspecifier(self):

        localctx = CPP14Parser.DeclspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_declspecifier)
        try:
            self.state = 1323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Extern, CPP14Parser.Mutable, CPP14Parser.Register, CPP14Parser.Static, CPP14Parser.Thread_local]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1317
                self.storageclassspecifier()
                pass
            elif token in [CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Class, CPP14Parser.Const, CPP14Parser.Decltype, CPP14Parser.Double, CPP14Parser.Enum, CPP14Parser.Float, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Struct, CPP14Parser.Typename, CPP14Parser.Union, CPP14Parser.Unsigned, CPP14Parser.Void, CPP14Parser.Volatile, CPP14Parser.Wchar, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1318
                self.typespecifier()
                pass
            elif token in [CPP14Parser.Explicit, CPP14Parser.Inline, CPP14Parser.Virtual]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1319
                self.functionspecifier()
                pass
            elif token in [CPP14Parser.Friend]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1320
                self.match(CPP14Parser.Friend)
                pass
            elif token in [CPP14Parser.Typedef]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1321
                self.match(CPP14Parser.Typedef)
                pass
            elif token in [CPP14Parser.Constexpr]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1322
                self.match(CPP14Parser.Constexpr)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclspecifierseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_declspecifierseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclspecifierseq" ):
                listener.enterDeclspecifierseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclspecifierseq" ):
                listener.exitDeclspecifierseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclspecifierseq" ):
                return visitor.visitDeclspecifierseq(self)
            else:
                return visitor.visitChildren(self)




    def declspecifierseq(self):

        localctx = CPP14Parser.DeclspecifierseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_declspecifierseq)
        try:
            self.state = 1332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1325
                self.declspecifier()
                self.state = 1327
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
                if la_ == 1:
                    self.state = 1326
                    self.attributespecifierseq(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1329
                self.declspecifier()
                self.state = 1330
                self.declspecifierseq()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StorageclassspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Register(self):
            return self.getToken(CPP14Parser.Register, 0)

        def Static(self):
            return self.getToken(CPP14Parser.Static, 0)

        def Thread_local(self):
            return self.getToken(CPP14Parser.Thread_local, 0)

        def Extern(self):
            return self.getToken(CPP14Parser.Extern, 0)

        def Mutable(self):
            return self.getToken(CPP14Parser.Mutable, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_storageclassspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStorageclassspecifier" ):
                listener.enterStorageclassspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStorageclassspecifier" ):
                listener.exitStorageclassspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStorageclassspecifier" ):
                return visitor.visitStorageclassspecifier(self)
            else:
                return visitor.visitChildren(self)




    def storageclassspecifier(self):

        localctx = CPP14Parser.StorageclassspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_storageclassspecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1334
            _la = self._input.LA(1)
            if not(((((_la - 31)) & ~0x3f) == 0 and ((1 << (_la - 31)) & ((1 << (CPP14Parser.Extern - 31)) | (1 << (CPP14Parser.Mutable - 31)) | (1 << (CPP14Parser.Register - 31)) | (1 << (CPP14Parser.Static - 31)) | (1 << (CPP14Parser.Thread_local - 31)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Inline(self):
            return self.getToken(CPP14Parser.Inline, 0)

        def Virtual(self):
            return self.getToken(CPP14Parser.Virtual, 0)

        def Explicit(self):
            return self.getToken(CPP14Parser.Explicit, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_functionspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionspecifier" ):
                listener.enterFunctionspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionspecifier" ):
                listener.exitFunctionspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionspecifier" ):
                return visitor.visitFunctionspecifier(self)
            else:
                return visitor.visitChildren(self)




    def functionspecifier(self):

        localctx = CPP14Parser.FunctionspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_functionspecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1336
            _la = self._input.LA(1)
            if not(((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & ((1 << (CPP14Parser.Explicit - 29)) | (1 << (CPP14Parser.Inline - 29)) | (1 << (CPP14Parser.Virtual - 29)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypedefnameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_typedefname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedefname" ):
                listener.enterTypedefname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedefname" ):
                listener.exitTypedefname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedefname" ):
                return visitor.visitTypedefname(self)
            else:
                return visitor.visitChildren(self)




    def typedefname(self):

        localctx = CPP14Parser.TypedefnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_typedefname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1338
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trailingtypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingtypespecifierContext,0)


        def classspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.ClassspecifierContext,0)


        def enumspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.EnumspecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_typespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypespecifier" ):
                listener.enterTypespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypespecifier" ):
                listener.exitTypespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypespecifier" ):
                return visitor.visitTypespecifier(self)
            else:
                return visitor.visitChildren(self)




    def typespecifier(self):

        localctx = CPP14Parser.TypespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_typespecifier)
        try:
            self.state = 1343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1340
                self.trailingtypespecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1341
                self.classspecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1342
                self.enumspecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrailingtypespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpletypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletypespecifierContext,0)


        def elaboratedtypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.ElaboratedtypespecifierContext,0)


        def typenamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.TypenamespecifierContext,0)


        def cvqualifier(self):
            return self.getTypedRuleContext(CPP14Parser.CvqualifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_trailingtypespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailingtypespecifier" ):
                listener.enterTrailingtypespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailingtypespecifier" ):
                listener.exitTrailingtypespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrailingtypespecifier" ):
                return visitor.visitTrailingtypespecifier(self)
            else:
                return visitor.visitChildren(self)




    def trailingtypespecifier(self):

        localctx = CPP14Parser.TrailingtypespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_trailingtypespecifier)
        try:
            self.state = 1349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Decltype, CPP14Parser.Double, CPP14Parser.Float, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Unsigned, CPP14Parser.Void, CPP14Parser.Wchar, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1345
                self.simpletypespecifier()
                pass
            elif token in [CPP14Parser.Class, CPP14Parser.Enum, CPP14Parser.Struct, CPP14Parser.Union]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1346
                self.elaboratedtypespecifier()
                pass
            elif token in [CPP14Parser.Typename]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1347
                self.typenamespecifier()
                pass
            elif token in [CPP14Parser.Const, CPP14Parser.Volatile]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1348
                self.cvqualifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypespecifierseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def typespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_typespecifierseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypespecifierseq" ):
                listener.enterTypespecifierseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypespecifierseq" ):
                listener.exitTypespecifierseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypespecifierseq" ):
                return visitor.visitTypespecifierseq(self)
            else:
                return visitor.visitChildren(self)




    def typespecifierseq(self):

        localctx = CPP14Parser.TypespecifierseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_typespecifierseq)
        try:
            self.state = 1358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1351
                self.typespecifier()
                self.state = 1353
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
                if la_ == 1:
                    self.state = 1352
                    self.attributespecifierseq(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1355
                self.typespecifier()
                self.state = 1356
                self.typespecifierseq()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrailingtypespecifierseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trailingtypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingtypespecifierContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def trailingtypespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingtypespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_trailingtypespecifierseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailingtypespecifierseq" ):
                listener.enterTrailingtypespecifierseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailingtypespecifierseq" ):
                listener.exitTrailingtypespecifierseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrailingtypespecifierseq" ):
                return visitor.visitTrailingtypespecifierseq(self)
            else:
                return visitor.visitChildren(self)




    def trailingtypespecifierseq(self):

        localctx = CPP14Parser.TrailingtypespecifierseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_trailingtypespecifierseq)
        try:
            self.state = 1367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1360
                self.trailingtypespecifier()
                self.state = 1362
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,124,self._ctx)
                if la_ == 1:
                    self.state = 1361
                    self.attributespecifierseq(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1364
                self.trailingtypespecifier()
                self.state = 1365
                self.trailingtypespecifierseq()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpletypespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(CPP14Parser.TypenameContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def Char(self):
            return self.getToken(CPP14Parser.Char, 0)

        def Char16(self):
            return self.getToken(CPP14Parser.Char16, 0)

        def Char32(self):
            return self.getToken(CPP14Parser.Char32, 0)

        def Wchar(self):
            return self.getToken(CPP14Parser.Wchar, 0)

        def Bool(self):
            return self.getToken(CPP14Parser.Bool, 0)

        def Short(self):
            return self.getToken(CPP14Parser.Short, 0)

        def Int(self):
            return self.getToken(CPP14Parser.Int, 0)

        def Long(self):
            return self.getToken(CPP14Parser.Long, 0)

        def Signed(self):
            return self.getToken(CPP14Parser.Signed, 0)

        def Unsigned(self):
            return self.getToken(CPP14Parser.Unsigned, 0)

        def Float(self):
            return self.getToken(CPP14Parser.Float, 0)

        def Double(self):
            return self.getToken(CPP14Parser.Double, 0)

        def Void(self):
            return self.getToken(CPP14Parser.Void, 0)

        def Auto(self):
            return self.getToken(CPP14Parser.Auto, 0)

        def decltypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.DecltypespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_simpletypespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpletypespecifier" ):
                listener.enterSimpletypespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpletypespecifier" ):
                listener.exitSimpletypespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpletypespecifier" ):
                return visitor.visitSimpletypespecifier(self)
            else:
                return visitor.visitChildren(self)




    def simpletypespecifier(self):

        localctx = CPP14Parser.SimpletypespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_simpletypespecifier)
        try:
            self.state = 1392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1370
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
                if la_ == 1:
                    self.state = 1369
                    self.nestednamespecifier(0)


                self.state = 1372
                self.typename()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1373
                self.nestednamespecifier(0)
                self.state = 1374
                self.match(CPP14Parser.Template)
                self.state = 1375
                self.simpletemplateid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1377
                self.match(CPP14Parser.Char)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1378
                self.match(CPP14Parser.Char16)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1379
                self.match(CPP14Parser.Char32)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1380
                self.match(CPP14Parser.Wchar)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1381
                self.match(CPP14Parser.Bool)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1382
                self.match(CPP14Parser.Short)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1383
                self.match(CPP14Parser.Int)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1384
                self.match(CPP14Parser.Long)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1385
                self.match(CPP14Parser.Signed)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1386
                self.match(CPP14Parser.Unsigned)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1387
                self.match(CPP14Parser.Float)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 1388
                self.match(CPP14Parser.Double)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 1389
                self.match(CPP14Parser.Void)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 1390
                self.match(CPP14Parser.Auto)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 1391
                self.decltypespecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypenameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(CPP14Parser.ClassnameContext,0)


        def enumname(self):
            return self.getTypedRuleContext(CPP14Parser.EnumnameContext,0)


        def typedefname(self):
            return self.getTypedRuleContext(CPP14Parser.TypedefnameContext,0)


        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_typename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypename" ):
                listener.enterTypename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypename" ):
                listener.exitTypename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypename" ):
                return visitor.visitTypename(self)
            else:
                return visitor.visitChildren(self)




    def typename(self):

        localctx = CPP14Parser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_typename)
        try:
            self.state = 1398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,128,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1394
                self.classname()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1395
                self.enumname()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1396
                self.typedefname()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1397
                self.simpletemplateid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DecltypespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Decltype(self):
            return self.getToken(CPP14Parser.Decltype, 0)

        def expression(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionContext,0)


        def Auto(self):
            return self.getToken(CPP14Parser.Auto, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_decltypespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecltypespecifier" ):
                listener.enterDecltypespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecltypespecifier" ):
                listener.exitDecltypespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecltypespecifier" ):
                return visitor.visitDecltypespecifier(self)
            else:
                return visitor.visitChildren(self)




    def decltypespecifier(self):

        localctx = CPP14Parser.DecltypespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_decltypespecifier)
        try:
            self.state = 1409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1400
                self.match(CPP14Parser.Decltype)
                self.state = 1401
                self.match(CPP14Parser.LeftParen)
                self.state = 1402
                self.expression(0)
                self.state = 1403
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1405
                self.match(CPP14Parser.Decltype)
                self.state = 1406
                self.match(CPP14Parser.LeftParen)
                self.state = 1407
                self.match(CPP14Parser.Auto)
                self.state = 1408
                self.match(CPP14Parser.RightParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElaboratedtypespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classkey(self):
            return self.getTypedRuleContext(CPP14Parser.ClasskeyContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def Enum(self):
            return self.getToken(CPP14Parser.Enum, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_elaboratedtypespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElaboratedtypespecifier" ):
                listener.enterElaboratedtypespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElaboratedtypespecifier" ):
                listener.exitElaboratedtypespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElaboratedtypespecifier" ):
                return visitor.visitElaboratedtypespecifier(self)
            else:
                return visitor.visitChildren(self)




    def elaboratedtypespecifier(self):

        localctx = CPP14Parser.ElaboratedtypespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_elaboratedtypespecifier)
        self._la = 0 # Token type
        try:
            self.state = 1435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1411
                self.classkey()
                self.state = 1413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1412
                    self.attributespecifierseq(0)


                self.state = 1416
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
                if la_ == 1:
                    self.state = 1415
                    self.nestednamespecifier(0)


                self.state = 1418
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1420
                self.classkey()
                self.state = 1421
                self.simpletemplateid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1423
                self.classkey()
                self.state = 1424
                self.nestednamespecifier(0)
                self.state = 1426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Template:
                    self.state = 1425
                    self.match(CPP14Parser.Template)


                self.state = 1428
                self.simpletemplateid()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1430
                self.match(CPP14Parser.Enum)
                self.state = 1432
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
                if la_ == 1:
                    self.state = 1431
                    self.nestednamespecifier(0)


                self.state = 1434
                self.match(CPP14Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumnameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_enumname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumname" ):
                listener.enterEnumname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumname" ):
                listener.exitEnumname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumname" ):
                return visitor.visitEnumname(self)
            else:
                return visitor.visitChildren(self)




    def enumname(self):

        localctx = CPP14Parser.EnumnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_enumname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1437
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumhead(self):
            return self.getTypedRuleContext(CPP14Parser.EnumheadContext,0)


        def enumeratorlist(self):
            return self.getTypedRuleContext(CPP14Parser.EnumeratorlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_enumspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumspecifier" ):
                listener.enterEnumspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumspecifier" ):
                listener.exitEnumspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumspecifier" ):
                return visitor.visitEnumspecifier(self)
            else:
                return visitor.visitChildren(self)




    def enumspecifier(self):

        localctx = CPP14Parser.EnumspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_enumspecifier)
        self._la = 0 # Token type
        try:
            self.state = 1452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1439
                self.enumhead()
                self.state = 1440
                self.match(CPP14Parser.LeftBrace)
                self.state = 1442
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Identifier:
                    self.state = 1441
                    self.enumeratorlist(0)


                self.state = 1444
                self.match(CPP14Parser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1446
                self.enumhead()
                self.state = 1447
                self.match(CPP14Parser.LeftBrace)
                self.state = 1448
                self.enumeratorlist(0)
                self.state = 1449
                self.match(CPP14Parser.Comma)
                self.state = 1450
                self.match(CPP14Parser.RightBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumheadContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumkey(self):
            return self.getTypedRuleContext(CPP14Parser.EnumkeyContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def enumbase(self):
            return self.getTypedRuleContext(CPP14Parser.EnumbaseContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_enumhead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumhead" ):
                listener.enterEnumhead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumhead" ):
                listener.exitEnumhead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumhead" ):
                return visitor.visitEnumhead(self)
            else:
                return visitor.visitChildren(self)




    def enumhead(self):

        localctx = CPP14Parser.EnumheadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_enumhead)
        self._la = 0 # Token type
        try:
            self.state = 1473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1454
                self.enumkey()
                self.state = 1456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1455
                    self.attributespecifierseq(0)


                self.state = 1459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Identifier:
                    self.state = 1458
                    self.match(CPP14Parser.Identifier)


                self.state = 1462
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Colon:
                    self.state = 1461
                    self.enumbase()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1464
                self.enumkey()
                self.state = 1466
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1465
                    self.attributespecifierseq(0)


                self.state = 1468
                self.nestednamespecifier(0)
                self.state = 1469
                self.match(CPP14Parser.Identifier)
                self.state = 1471
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Colon:
                    self.state = 1470
                    self.enumbase()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpaqueenumdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumkey(self):
            return self.getTypedRuleContext(CPP14Parser.EnumkeyContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def enumbase(self):
            return self.getTypedRuleContext(CPP14Parser.EnumbaseContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_opaqueenumdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpaqueenumdeclaration" ):
                listener.enterOpaqueenumdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpaqueenumdeclaration" ):
                listener.exitOpaqueenumdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpaqueenumdeclaration" ):
                return visitor.visitOpaqueenumdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def opaqueenumdeclaration(self):

        localctx = CPP14Parser.OpaqueenumdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_opaqueenumdeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1475
            self.enumkey()
            self.state = 1477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 1476
                self.attributespecifierseq(0)


            self.state = 1479
            self.match(CPP14Parser.Identifier)
            self.state = 1481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Colon:
                self.state = 1480
                self.enumbase()


            self.state = 1483
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumkeyContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Enum(self):
            return self.getToken(CPP14Parser.Enum, 0)

        def Class(self):
            return self.getToken(CPP14Parser.Class, 0)

        def Struct(self):
            return self.getToken(CPP14Parser.Struct, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_enumkey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumkey" ):
                listener.enterEnumkey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumkey" ):
                listener.exitEnumkey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumkey" ):
                return visitor.visitEnumkey(self)
            else:
                return visitor.visitChildren(self)




    def enumkey(self):

        localctx = CPP14Parser.EnumkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_enumkey)
        try:
            self.state = 1490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,145,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1485
                self.match(CPP14Parser.Enum)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1486
                self.match(CPP14Parser.Enum)
                self.state = 1487
                self.match(CPP14Parser.Class)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1488
                self.match(CPP14Parser.Enum)
                self.state = 1489
                self.match(CPP14Parser.Struct)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumbaseContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_enumbase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumbase" ):
                listener.enterEnumbase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumbase" ):
                listener.exitEnumbase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumbase" ):
                return visitor.visitEnumbase(self)
            else:
                return visitor.visitChildren(self)




    def enumbase(self):

        localctx = CPP14Parser.EnumbaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_enumbase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1492
            self.match(CPP14Parser.Colon)
            self.state = 1493
            self.typespecifierseq()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumeratorlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumeratordefinition(self):
            return self.getTypedRuleContext(CPP14Parser.EnumeratordefinitionContext,0)


        def enumeratorlist(self):
            return self.getTypedRuleContext(CPP14Parser.EnumeratorlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_enumeratorlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumeratorlist" ):
                listener.enterEnumeratorlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumeratorlist" ):
                listener.exitEnumeratorlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumeratorlist" ):
                return visitor.visitEnumeratorlist(self)
            else:
                return visitor.visitChildren(self)



    def enumeratorlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.EnumeratorlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 186
        self.enterRecursionRule(localctx, 186, self.RULE_enumeratorlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1496
            self.enumeratordefinition()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,146,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.EnumeratorlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_enumeratorlist)
                    self.state = 1498
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1499
                    self.match(CPP14Parser.Comma)
                    self.state = 1500
                    self.enumeratordefinition() 
                self.state = 1505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,146,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class EnumeratordefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumerator(self):
            return self.getTypedRuleContext(CPP14Parser.EnumeratorContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_enumeratordefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumeratordefinition" ):
                listener.enterEnumeratordefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumeratordefinition" ):
                listener.exitEnumeratordefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumeratordefinition" ):
                return visitor.visitEnumeratordefinition(self)
            else:
                return visitor.visitChildren(self)




    def enumeratordefinition(self):

        localctx = CPP14Parser.EnumeratordefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_enumeratordefinition)
        try:
            self.state = 1511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1506
                self.enumerator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1507
                self.enumerator()
                self.state = 1508
                self.match(CPP14Parser.Assign)
                self.state = 1509
                self.constantexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumeratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_enumerator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumerator" ):
                listener.enterEnumerator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumerator" ):
                listener.exitEnumerator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumerator" ):
                return visitor.visitEnumerator(self)
            else:
                return visitor.visitChildren(self)




    def enumerator(self):

        localctx = CPP14Parser.EnumeratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_enumerator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1513
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamespacenameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def originalnamespacename(self):
            return self.getTypedRuleContext(CPP14Parser.OriginalnamespacenameContext,0)


        def namespacealias(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacealiasContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_namespacename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespacename" ):
                listener.enterNamespacename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespacename" ):
                listener.exitNamespacename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespacename" ):
                return visitor.visitNamespacename(self)
            else:
                return visitor.visitChildren(self)




    def namespacename(self):

        localctx = CPP14Parser.NamespacenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_namespacename)
        try:
            self.state = 1517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1515
                self.originalnamespacename()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1516
                self.namespacealias()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OriginalnamespacenameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_originalnamespacename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOriginalnamespacename" ):
                listener.enterOriginalnamespacename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOriginalnamespacename" ):
                listener.exitOriginalnamespacename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOriginalnamespacename" ):
                return visitor.visitOriginalnamespacename(self)
            else:
                return visitor.visitChildren(self)




    def originalnamespacename(self):

        localctx = CPP14Parser.OriginalnamespacenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_originalnamespacename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1519
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamespacedefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namednamespacedefinition(self):
            return self.getTypedRuleContext(CPP14Parser.NamednamespacedefinitionContext,0)


        def unnamednamespacedefinition(self):
            return self.getTypedRuleContext(CPP14Parser.UnnamednamespacedefinitionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_namespacedefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespacedefinition" ):
                listener.enterNamespacedefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespacedefinition" ):
                listener.exitNamespacedefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespacedefinition" ):
                return visitor.visitNamespacedefinition(self)
            else:
                return visitor.visitChildren(self)




    def namespacedefinition(self):

        localctx = CPP14Parser.NamespacedefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_namespacedefinition)
        try:
            self.state = 1523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,149,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1521
                self.namednamespacedefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1522
                self.unnamednamespacedefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamednamespacedefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def originalnamespacedefinition(self):
            return self.getTypedRuleContext(CPP14Parser.OriginalnamespacedefinitionContext,0)


        def extensionnamespacedefinition(self):
            return self.getTypedRuleContext(CPP14Parser.ExtensionnamespacedefinitionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_namednamespacedefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamednamespacedefinition" ):
                listener.enterNamednamespacedefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamednamespacedefinition" ):
                listener.exitNamednamespacedefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamednamespacedefinition" ):
                return visitor.visitNamednamespacedefinition(self)
            else:
                return visitor.visitChildren(self)




    def namednamespacedefinition(self):

        localctx = CPP14Parser.NamednamespacedefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_namednamespacedefinition)
        try:
            self.state = 1527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,150,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1525
                self.originalnamespacedefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1526
                self.extensionnamespacedefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OriginalnamespacedefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Namespace(self):
            return self.getToken(CPP14Parser.Namespace, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def namespacebody(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacebodyContext,0)


        def Inline(self):
            return self.getToken(CPP14Parser.Inline, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_originalnamespacedefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOriginalnamespacedefinition" ):
                listener.enterOriginalnamespacedefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOriginalnamespacedefinition" ):
                listener.exitOriginalnamespacedefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOriginalnamespacedefinition" ):
                return visitor.visitOriginalnamespacedefinition(self)
            else:
                return visitor.visitChildren(self)




    def originalnamespacedefinition(self):

        localctx = CPP14Parser.OriginalnamespacedefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_originalnamespacedefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1530
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Inline:
                self.state = 1529
                self.match(CPP14Parser.Inline)


            self.state = 1532
            self.match(CPP14Parser.Namespace)
            self.state = 1533
            self.match(CPP14Parser.Identifier)
            self.state = 1534
            self.match(CPP14Parser.LeftBrace)
            self.state = 1535
            self.namespacebody()
            self.state = 1536
            self.match(CPP14Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExtensionnamespacedefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Namespace(self):
            return self.getToken(CPP14Parser.Namespace, 0)

        def originalnamespacename(self):
            return self.getTypedRuleContext(CPP14Parser.OriginalnamespacenameContext,0)


        def namespacebody(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacebodyContext,0)


        def Inline(self):
            return self.getToken(CPP14Parser.Inline, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_extensionnamespacedefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtensionnamespacedefinition" ):
                listener.enterExtensionnamespacedefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtensionnamespacedefinition" ):
                listener.exitExtensionnamespacedefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtensionnamespacedefinition" ):
                return visitor.visitExtensionnamespacedefinition(self)
            else:
                return visitor.visitChildren(self)




    def extensionnamespacedefinition(self):

        localctx = CPP14Parser.ExtensionnamespacedefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_extensionnamespacedefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Inline:
                self.state = 1538
                self.match(CPP14Parser.Inline)


            self.state = 1541
            self.match(CPP14Parser.Namespace)
            self.state = 1542
            self.originalnamespacename()
            self.state = 1543
            self.match(CPP14Parser.LeftBrace)
            self.state = 1544
            self.namespacebody()
            self.state = 1545
            self.match(CPP14Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnnamednamespacedefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Namespace(self):
            return self.getToken(CPP14Parser.Namespace, 0)

        def namespacebody(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacebodyContext,0)


        def Inline(self):
            return self.getToken(CPP14Parser.Inline, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_unnamednamespacedefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnnamednamespacedefinition" ):
                listener.enterUnnamednamespacedefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnnamednamespacedefinition" ):
                listener.exitUnnamednamespacedefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnnamednamespacedefinition" ):
                return visitor.visitUnnamednamespacedefinition(self)
            else:
                return visitor.visitChildren(self)




    def unnamednamespacedefinition(self):

        localctx = CPP14Parser.UnnamednamespacedefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_unnamednamespacedefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Inline:
                self.state = 1547
                self.match(CPP14Parser.Inline)


            self.state = 1550
            self.match(CPP14Parser.Namespace)
            self.state = 1551
            self.match(CPP14Parser.LeftBrace)
            self.state = 1552
            self.namespacebody()
            self.state = 1553
            self.match(CPP14Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamespacebodyContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_namespacebody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespacebody" ):
                listener.enterNamespacebody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespacebody" ):
                listener.exitNamespacebody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespacebody" ):
                return visitor.visitNamespacebody(self)
            else:
                return visitor.visitChildren(self)




    def namespacebody(self):

        localctx = CPP14Parser.NamespacebodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_namespacebody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Asm) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Namespace) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Template))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Using - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftParen - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Star - 65)) | (1 << (CPP14Parser.And - 65)) | (1 << (CPP14Parser.Tilde - 65)) | (1 << (CPP14Parser.AndAnd - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Semi - 65)) | (1 << (CPP14Parser.Ellipsis - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                self.state = 1555
                self.declarationseq(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamespacealiasContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_namespacealias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespacealias" ):
                listener.enterNamespacealias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespacealias" ):
                listener.exitNamespacealias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespacealias" ):
                return visitor.visitNamespacealias(self)
            else:
                return visitor.visitChildren(self)




    def namespacealias(self):

        localctx = CPP14Parser.NamespacealiasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_namespacealias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1558
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NamespacealiasdefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Namespace(self):
            return self.getToken(CPP14Parser.Namespace, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def qualifiednamespacespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.QualifiednamespacespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_namespacealiasdefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespacealiasdefinition" ):
                listener.enterNamespacealiasdefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespacealiasdefinition" ):
                listener.exitNamespacealiasdefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespacealiasdefinition" ):
                return visitor.visitNamespacealiasdefinition(self)
            else:
                return visitor.visitChildren(self)




    def namespacealiasdefinition(self):

        localctx = CPP14Parser.NamespacealiasdefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_namespacealiasdefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1560
            self.match(CPP14Parser.Namespace)
            self.state = 1561
            self.match(CPP14Parser.Identifier)
            self.state = 1562
            self.match(CPP14Parser.Assign)
            self.state = 1563
            self.qualifiednamespacespecifier()
            self.state = 1564
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QualifiednamespacespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespacename(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacenameContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_qualifiednamespacespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiednamespacespecifier" ):
                listener.enterQualifiednamespacespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiednamespacespecifier" ):
                listener.exitQualifiednamespacespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiednamespacespecifier" ):
                return visitor.visitQualifiednamespacespecifier(self)
            else:
                return visitor.visitChildren(self)




    def qualifiednamespacespecifier(self):

        localctx = CPP14Parser.QualifiednamespacespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_qualifiednamespacespecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,155,self._ctx)
            if la_ == 1:
                self.state = 1566
                self.nestednamespecifier(0)


            self.state = 1569
            self.namespacename()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UsingdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Using(self):
            return self.getToken(CPP14Parser.Using, 0)

        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def unqualifiedid(self):
            return self.getTypedRuleContext(CPP14Parser.UnqualifiedidContext,0)


        def Typename(self):
            return self.getToken(CPP14Parser.Typename, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_usingdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingdeclaration" ):
                listener.enterUsingdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingdeclaration" ):
                listener.exitUsingdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsingdeclaration" ):
                return visitor.visitUsingdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def usingdeclaration(self):

        localctx = CPP14Parser.UsingdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_usingdeclaration)
        self._la = 0 # Token type
        try:
            self.state = 1584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1571
                self.match(CPP14Parser.Using)
                self.state = 1573
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Typename:
                    self.state = 1572
                    self.match(CPP14Parser.Typename)


                self.state = 1575
                self.nestednamespecifier(0)
                self.state = 1576
                self.unqualifiedid()
                self.state = 1577
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1579
                self.match(CPP14Parser.Using)
                self.state = 1580
                self.match(CPP14Parser.Doublecolon)
                self.state = 1581
                self.unqualifiedid()
                self.state = 1582
                self.match(CPP14Parser.Semi)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UsingdirectiveContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Using(self):
            return self.getToken(CPP14Parser.Using, 0)

        def Namespace(self):
            return self.getToken(CPP14Parser.Namespace, 0)

        def namespacename(self):
            return self.getTypedRuleContext(CPP14Parser.NamespacenameContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_usingdirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingdirective" ):
                listener.enterUsingdirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingdirective" ):
                listener.exitUsingdirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsingdirective" ):
                return visitor.visitUsingdirective(self)
            else:
                return visitor.visitChildren(self)




    def usingdirective(self):

        localctx = CPP14Parser.UsingdirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_usingdirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1587
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 1586
                self.attributespecifierseq(0)


            self.state = 1589
            self.match(CPP14Parser.Using)
            self.state = 1590
            self.match(CPP14Parser.Namespace)
            self.state = 1592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,159,self._ctx)
            if la_ == 1:
                self.state = 1591
                self.nestednamespecifier(0)


            self.state = 1594
            self.namespacename()
            self.state = 1595
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsmdefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Asm(self):
            return self.getToken(CPP14Parser.Asm, 0)

        def Stringliteral(self):
            return self.getToken(CPP14Parser.Stringliteral, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_asmdefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsmdefinition" ):
                listener.enterAsmdefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsmdefinition" ):
                listener.exitAsmdefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsmdefinition" ):
                return visitor.visitAsmdefinition(self)
            else:
                return visitor.visitChildren(self)




    def asmdefinition(self):

        localctx = CPP14Parser.AsmdefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_asmdefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1597
            self.match(CPP14Parser.Asm)
            self.state = 1598
            self.match(CPP14Parser.LeftParen)
            self.state = 1599
            self.match(CPP14Parser.Stringliteral)
            self.state = 1600
            self.match(CPP14Parser.RightParen)
            self.state = 1601
            self.match(CPP14Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LinkagespecificationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Extern(self):
            return self.getToken(CPP14Parser.Extern, 0)

        def Stringliteral(self):
            return self.getToken(CPP14Parser.Stringliteral, 0)

        def declarationseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationseqContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_linkagespecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkagespecification" ):
                listener.enterLinkagespecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkagespecification" ):
                listener.exitLinkagespecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkagespecification" ):
                return visitor.visitLinkagespecification(self)
            else:
                return visitor.visitChildren(self)




    def linkagespecification(self):

        localctx = CPP14Parser.LinkagespecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_linkagespecification)
        self._la = 0 # Token type
        try:
            self.state = 1613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1603
                self.match(CPP14Parser.Extern)
                self.state = 1604
                self.match(CPP14Parser.Stringliteral)
                self.state = 1605
                self.match(CPP14Parser.LeftBrace)
                self.state = 1607
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Asm) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Namespace) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Template))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Using - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftParen - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Star - 65)) | (1 << (CPP14Parser.And - 65)) | (1 << (CPP14Parser.Tilde - 65)) | (1 << (CPP14Parser.AndAnd - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Semi - 65)) | (1 << (CPP14Parser.Ellipsis - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                    self.state = 1606
                    self.declarationseq(0)


                self.state = 1609
                self.match(CPP14Parser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1610
                self.match(CPP14Parser.Extern)
                self.state = 1611
                self.match(CPP14Parser.Stringliteral)
                self.state = 1612
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributespecifierseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attributespecifierseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributespecifierseq" ):
                listener.enterAttributespecifierseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributespecifierseq" ):
                listener.exitAttributespecifierseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributespecifierseq" ):
                return visitor.visitAttributespecifierseq(self)
            else:
                return visitor.visitChildren(self)



    def attributespecifierseq(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.AttributespecifierseqContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 222
        self.enterRecursionRule(localctx, 222, self.RULE_attributespecifierseq, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1616
            self.attributespecifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1622
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.AttributespecifierseqContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_attributespecifierseq)
                    self.state = 1618
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1619
                    self.attributespecifier() 
                self.state = 1624
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AttributespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributelist(self):
            return self.getTypedRuleContext(CPP14Parser.AttributelistContext,0)


        def alignmentspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.AlignmentspecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attributespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributespecifier" ):
                listener.enterAttributespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributespecifier" ):
                listener.exitAttributespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributespecifier" ):
                return visitor.visitAttributespecifier(self)
            else:
                return visitor.visitChildren(self)




    def attributespecifier(self):

        localctx = CPP14Parser.AttributespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_attributespecifier)
        try:
            self.state = 1632
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1625
                self.match(CPP14Parser.LeftBracket)
                self.state = 1626
                self.match(CPP14Parser.LeftBracket)
                self.state = 1627
                self.attributelist(0)
                self.state = 1628
                self.match(CPP14Parser.RightBracket)
                self.state = 1629
                self.match(CPP14Parser.RightBracket)
                pass
            elif token in [CPP14Parser.Alignas]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1631
                self.alignmentspecifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlignmentspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Alignas(self):
            return self.getToken(CPP14Parser.Alignas, 0)

        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_alignmentspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlignmentspecifier" ):
                listener.enterAlignmentspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlignmentspecifier" ):
                listener.exitAlignmentspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlignmentspecifier" ):
                return visitor.visitAlignmentspecifier(self)
            else:
                return visitor.visitChildren(self)




    def alignmentspecifier(self):

        localctx = CPP14Parser.AlignmentspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_alignmentspecifier)
        self._la = 0 # Token type
        try:
            self.state = 1650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,166,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1634
                self.match(CPP14Parser.Alignas)
                self.state = 1635
                self.match(CPP14Parser.LeftParen)
                self.state = 1636
                self.typeid()
                self.state = 1638
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Ellipsis:
                    self.state = 1637
                    self.match(CPP14Parser.Ellipsis)


                self.state = 1640
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1642
                self.match(CPP14Parser.Alignas)
                self.state = 1643
                self.match(CPP14Parser.LeftParen)
                self.state = 1644
                self.constantexpression()
                self.state = 1646
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Ellipsis:
                    self.state = 1645
                    self.match(CPP14Parser.Ellipsis)


                self.state = 1648
                self.match(CPP14Parser.RightParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributelistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CPP14Parser.AttributeContext,0)


        def attributelist(self):
            return self.getTypedRuleContext(CPP14Parser.AttributelistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attributelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributelist" ):
                listener.enterAttributelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributelist" ):
                listener.exitAttributelist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributelist" ):
                return visitor.visitAttributelist(self)
            else:
                return visitor.visitChildren(self)



    def attributelist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.AttributelistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 228
        self.enterRecursionRule(localctx, 228, self.RULE_attributelist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1659
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,168,self._ctx)
            if la_ == 1:
                self.state = 1654
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,167,self._ctx)
                if la_ == 1:
                    self.state = 1653
                    self.attribute()


                pass

            elif la_ == 2:
                self.state = 1656
                self.attribute()
                self.state = 1657
                self.match(CPP14Parser.Ellipsis)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1673
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1671
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,170,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.AttributelistContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attributelist)
                        self.state = 1661
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1662
                        self.match(CPP14Parser.Comma)
                        self.state = 1664
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,169,self._ctx)
                        if la_ == 1:
                            self.state = 1663
                            self.attribute()


                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.AttributelistContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_attributelist)
                        self.state = 1666
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 1667
                        self.match(CPP14Parser.Comma)
                        self.state = 1668
                        self.attribute()
                        self.state = 1669
                        self.match(CPP14Parser.Ellipsis)
                        pass

             
                self.state = 1675
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AttributeContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributetoken(self):
            return self.getTypedRuleContext(CPP14Parser.AttributetokenContext,0)


        def attributeargumentclause(self):
            return self.getTypedRuleContext(CPP14Parser.AttributeargumentclauseContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = CPP14Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1676
            self.attributetoken()
            self.state = 1678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,172,self._ctx)
            if la_ == 1:
                self.state = 1677
                self.attributeargumentclause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributetokenContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def attributescopedtoken(self):
            return self.getTypedRuleContext(CPP14Parser.AttributescopedtokenContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attributetoken

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributetoken" ):
                listener.enterAttributetoken(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributetoken" ):
                listener.exitAttributetoken(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributetoken" ):
                return visitor.visitAttributetoken(self)
            else:
                return visitor.visitChildren(self)




    def attributetoken(self):

        localctx = CPP14Parser.AttributetokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_attributetoken)
        try:
            self.state = 1682
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1680
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1681
                self.attributescopedtoken()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributescopedtokenContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributenamespace(self):
            return self.getTypedRuleContext(CPP14Parser.AttributenamespaceContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_attributescopedtoken

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributescopedtoken" ):
                listener.enterAttributescopedtoken(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributescopedtoken" ):
                listener.exitAttributescopedtoken(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributescopedtoken" ):
                return visitor.visitAttributescopedtoken(self)
            else:
                return visitor.visitChildren(self)




    def attributescopedtoken(self):

        localctx = CPP14Parser.AttributescopedtokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_attributescopedtoken)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1684
            self.attributenamespace()
            self.state = 1685
            self.match(CPP14Parser.Doublecolon)
            self.state = 1686
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributenamespaceContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_attributenamespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributenamespace" ):
                listener.enterAttributenamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributenamespace" ):
                listener.exitAttributenamespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributenamespace" ):
                return visitor.visitAttributenamespace(self)
            else:
                return visitor.visitChildren(self)




    def attributenamespace(self):

        localctx = CPP14Parser.AttributenamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_attributenamespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1688
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeargumentclauseContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def balancedtokenseq(self):
            return self.getTypedRuleContext(CPP14Parser.BalancedtokenseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_attributeargumentclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeargumentclause" ):
                listener.enterAttributeargumentclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeargumentclause" ):
                listener.exitAttributeargumentclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeargumentclause" ):
                return visitor.visitAttributeargumentclause(self)
            else:
                return visitor.visitChildren(self)




    def attributeargumentclause(self):

        localctx = CPP14Parser.AttributeargumentclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_attributeargumentclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1690
            self.match(CPP14Parser.LeftParen)
            self.state = 1691
            self.balancedtokenseq(0)
            self.state = 1692
            self.match(CPP14Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BalancedtokenseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def balancedtoken(self):
            return self.getTypedRuleContext(CPP14Parser.BalancedtokenContext,0)


        def balancedtokenseq(self):
            return self.getTypedRuleContext(CPP14Parser.BalancedtokenseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_balancedtokenseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBalancedtokenseq" ):
                listener.enterBalancedtokenseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBalancedtokenseq" ):
                listener.exitBalancedtokenseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBalancedtokenseq" ):
                return visitor.visitBalancedtokenseq(self)
            else:
                return visitor.visitChildren(self)



    def balancedtokenseq(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.BalancedtokenseqContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 240
        self.enterRecursionRule(localctx, 240, self.RULE_balancedtokenseq, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1696
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,174,self._ctx)
            if la_ == 1:
                self.state = 1695
                self.balancedtoken()


            self._ctx.stop = self._input.LT(-1)
            self.state = 1702
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,175,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.BalancedtokenseqContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_balancedtokenseq)
                    self.state = 1698
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1699
                    self.balancedtoken() 
                self.state = 1704
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,175,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BalancedtokenContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def balancedtokenseq(self):
            return self.getTypedRuleContext(CPP14Parser.BalancedtokenseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_balancedtoken

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBalancedtoken" ):
                listener.enterBalancedtoken(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBalancedtoken" ):
                listener.exitBalancedtoken(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBalancedtoken" ):
                return visitor.visitBalancedtoken(self)
            else:
                return visitor.visitChildren(self)




    def balancedtoken(self):

        localctx = CPP14Parser.BalancedtokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_balancedtoken)
        try:
            self.state = 1717
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.LeftParen]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1705
                self.match(CPP14Parser.LeftParen)
                self.state = 1706
                self.balancedtokenseq(0)
                self.state = 1707
                self.match(CPP14Parser.RightParen)
                pass
            elif token in [CPP14Parser.LeftBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1709
                self.match(CPP14Parser.LeftBracket)
                self.state = 1710
                self.balancedtokenseq(0)
                self.state = 1711
                self.match(CPP14Parser.RightBracket)
                pass
            elif token in [CPP14Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1713
                self.match(CPP14Parser.LeftBrace)
                self.state = 1714
                self.balancedtokenseq(0)
                self.state = 1715
                self.match(CPP14Parser.RightBrace)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitdeclaratorlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.InitdeclaratorContext,0)


        def initdeclaratorlist(self):
            return self.getTypedRuleContext(CPP14Parser.InitdeclaratorlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_initdeclaratorlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitdeclaratorlist" ):
                listener.enterInitdeclaratorlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitdeclaratorlist" ):
                listener.exitInitdeclaratorlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitdeclaratorlist" ):
                return visitor.visitInitdeclaratorlist(self)
            else:
                return visitor.visitChildren(self)



    def initdeclaratorlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.InitdeclaratorlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 244
        self.enterRecursionRule(localctx, 244, self.RULE_initdeclaratorlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720
            self.initdeclarator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1727
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,177,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.InitdeclaratorlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initdeclaratorlist)
                    self.state = 1722
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1723
                    self.match(CPP14Parser.Comma)
                    self.state = 1724
                    self.initdeclarator() 
                self.state = 1729
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,177,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class InitdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def initializer(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_initdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitdeclarator" ):
                listener.enterInitdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitdeclarator" ):
                listener.exitInitdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitdeclarator" ):
                return visitor.visitInitdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def initdeclarator(self):

        localctx = CPP14Parser.InitdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_initdeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1730
            self.declarator()
            self.state = 1732
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,178,self._ctx)
            if la_ == 1:
                self.state = 1731
                self.initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ptrdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.PtrdeclaratorContext,0)


        def noptrdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrdeclaratorContext,0)


        def parametersandqualifiers(self):
            return self.getTypedRuleContext(CPP14Parser.ParametersandqualifiersContext,0)


        def trailingreturntype(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingreturntypeContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarator" ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarator" ):
                listener.exitDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarator" ):
                return visitor.visitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def declarator(self):

        localctx = CPP14Parser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_declarator)
        try:
            self.state = 1739
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1734
                self.ptrdeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1735
                self.noptrdeclarator(0)
                self.state = 1736
                self.parametersandqualifiers()
                self.state = 1737
                self.trailingreturntype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PtrdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noptrdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrdeclaratorContext,0)


        def ptroperator(self):
            return self.getTypedRuleContext(CPP14Parser.PtroperatorContext,0)


        def ptrdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.PtrdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_ptrdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtrdeclarator" ):
                listener.enterPtrdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtrdeclarator" ):
                listener.exitPtrdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPtrdeclarator" ):
                return visitor.visitPtrdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def ptrdeclarator(self):

        localctx = CPP14Parser.PtrdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_ptrdeclarator)
        try:
            self.state = 1745
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,180,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1741
                self.noptrdeclarator(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1742
                self.ptroperator()
                self.state = 1743
                self.ptrdeclarator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoptrdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaratorid(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratoridContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def ptrdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.PtrdeclaratorContext,0)


        def noptrdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrdeclaratorContext,0)


        def parametersandqualifiers(self):
            return self.getTypedRuleContext(CPP14Parser.ParametersandqualifiersContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_noptrdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoptrdeclarator" ):
                listener.enterNoptrdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoptrdeclarator" ):
                listener.exitNoptrdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoptrdeclarator" ):
                return visitor.visitNoptrdeclarator(self)
            else:
                return visitor.visitChildren(self)



    def noptrdeclarator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.NoptrdeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 252
        self.enterRecursionRule(localctx, 252, self.RULE_noptrdeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1756
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Decltype, CPP14Parser.Operator, CPP14Parser.Tilde, CPP14Parser.Doublecolon, CPP14Parser.Ellipsis, CPP14Parser.Identifier]:
                self.state = 1748
                self.declaratorid()
                self.state = 1750
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,181,self._ctx)
                if la_ == 1:
                    self.state = 1749
                    self.attributespecifierseq(0)


                pass
            elif token in [CPP14Parser.LeftParen]:
                self.state = 1752
                self.match(CPP14Parser.LeftParen)
                self.state = 1753
                self.ptrdeclarator()
                self.state = 1754
                self.match(CPP14Parser.RightParen)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 1771
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,186,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1769
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,185,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.NoptrdeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrdeclarator)
                        self.state = 1758
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1759
                        self.parametersandqualifiers()
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.NoptrdeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrdeclarator)
                        self.state = 1760
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1761
                        self.match(CPP14Parser.LeftBracket)
                        self.state = 1763
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                            self.state = 1762
                            self.constantexpression()


                        self.state = 1765
                        self.match(CPP14Parser.RightBracket)
                        self.state = 1767
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,184,self._ctx)
                        if la_ == 1:
                            self.state = 1766
                            self.attributespecifierseq(0)


                        pass

             
                self.state = 1773
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,186,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParametersandqualifiersContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterdeclarationclause(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterdeclarationclauseContext,0)


        def cvqualifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.CvqualifierseqContext,0)


        def refqualifier(self):
            return self.getTypedRuleContext(CPP14Parser.RefqualifierContext,0)


        def exceptionspecification(self):
            return self.getTypedRuleContext(CPP14Parser.ExceptionspecificationContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_parametersandqualifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametersandqualifiers" ):
                listener.enterParametersandqualifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametersandqualifiers" ):
                listener.exitParametersandqualifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersandqualifiers" ):
                return visitor.visitParametersandqualifiers(self)
            else:
                return visitor.visitChildren(self)




    def parametersandqualifiers(self):

        localctx = CPP14Parser.ParametersandqualifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_parametersandqualifiers)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1774
            self.match(CPP14Parser.LeftParen)
            self.state = 1775
            self.parameterdeclarationclause()
            self.state = 1776
            self.match(CPP14Parser.RightParen)
            self.state = 1778
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,187,self._ctx)
            if la_ == 1:
                self.state = 1777
                self.cvqualifierseq()


            self.state = 1781
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,188,self._ctx)
            if la_ == 1:
                self.state = 1780
                self.refqualifier()


            self.state = 1784
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,189,self._ctx)
            if la_ == 1:
                self.state = 1783
                self.exceptionspecification()


            self.state = 1787
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.state = 1786
                self.attributespecifierseq(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrailingreturntypeContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trailingtypespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingtypespecifierseqContext,0)


        def abstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.AbstractdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_trailingreturntype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailingreturntype" ):
                listener.enterTrailingreturntype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailingreturntype" ):
                listener.exitTrailingreturntype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrailingreturntype" ):
                return visitor.visitTrailingreturntype(self)
            else:
                return visitor.visitChildren(self)




    def trailingreturntype(self):

        localctx = CPP14Parser.TrailingreturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_trailingreturntype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1789
            self.match(CPP14Parser.Arrow)
            self.state = 1790
            self.trailingtypespecifierseq()
            self.state = 1792
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,191,self._ctx)
            if la_ == 1:
                self.state = 1791
                self.abstractdeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PtroperatorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def cvqualifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.CvqualifierseqContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_ptroperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtroperator" ):
                listener.enterPtroperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtroperator" ):
                listener.exitPtroperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPtroperator" ):
                return visitor.visitPtroperator(self)
            else:
                return visitor.visitChildren(self)




    def ptroperator(self):

        localctx = CPP14Parser.PtroperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_ptroperator)
        try:
            self.state = 1817
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Star]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1794
                self.match(CPP14Parser.Star)
                self.state = 1796
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,192,self._ctx)
                if la_ == 1:
                    self.state = 1795
                    self.attributespecifierseq(0)


                self.state = 1799
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,193,self._ctx)
                if la_ == 1:
                    self.state = 1798
                    self.cvqualifierseq()


                pass
            elif token in [CPP14Parser.And]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1801
                self.match(CPP14Parser.And)
                self.state = 1803
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,194,self._ctx)
                if la_ == 1:
                    self.state = 1802
                    self.attributespecifierseq(0)


                pass
            elif token in [CPP14Parser.AndAnd]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1805
                self.match(CPP14Parser.AndAnd)
                self.state = 1807
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,195,self._ctx)
                if la_ == 1:
                    self.state = 1806
                    self.attributespecifierseq(0)


                pass
            elif token in [CPP14Parser.Decltype, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1809
                self.nestednamespecifier(0)
                self.state = 1810
                self.match(CPP14Parser.Star)
                self.state = 1812
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,196,self._ctx)
                if la_ == 1:
                    self.state = 1811
                    self.attributespecifierseq(0)


                self.state = 1815
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,197,self._ctx)
                if la_ == 1:
                    self.state = 1814
                    self.cvqualifierseq()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CvqualifierseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cvqualifier(self):
            return self.getTypedRuleContext(CPP14Parser.CvqualifierContext,0)


        def cvqualifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.CvqualifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_cvqualifierseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvqualifierseq" ):
                listener.enterCvqualifierseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvqualifierseq" ):
                listener.exitCvqualifierseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCvqualifierseq" ):
                return visitor.visitCvqualifierseq(self)
            else:
                return visitor.visitChildren(self)




    def cvqualifierseq(self):

        localctx = CPP14Parser.CvqualifierseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_cvqualifierseq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1819
            self.cvqualifier()
            self.state = 1821
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,199,self._ctx)
            if la_ == 1:
                self.state = 1820
                self.cvqualifierseq()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CvqualifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Const(self):
            return self.getToken(CPP14Parser.Const, 0)

        def Volatile(self):
            return self.getToken(CPP14Parser.Volatile, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_cvqualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvqualifier" ):
                listener.enterCvqualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvqualifier" ):
                listener.exitCvqualifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCvqualifier" ):
                return visitor.visitCvqualifier(self)
            else:
                return visitor.visitChildren(self)




    def cvqualifier(self):

        localctx = CPP14Parser.CvqualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_cvqualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1823
            _la = self._input.LA(1)
            if not(_la==CPP14Parser.Const or _la==CPP14Parser.Volatile):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RefqualifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPP14Parser.RULE_refqualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRefqualifier" ):
                listener.enterRefqualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRefqualifier" ):
                listener.exitRefqualifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefqualifier" ):
                return visitor.visitRefqualifier(self)
            else:
                return visitor.visitChildren(self)




    def refqualifier(self):

        localctx = CPP14Parser.RefqualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_refqualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1825
            _la = self._input.LA(1)
            if not(_la==CPP14Parser.And or _la==CPP14Parser.AndAnd):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaratoridContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idexpression(self):
            return self.getTypedRuleContext(CPP14Parser.IdexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_declaratorid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaratorid" ):
                listener.enterDeclaratorid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaratorid" ):
                listener.exitDeclaratorid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaratorid" ):
                return visitor.visitDeclaratorid(self)
            else:
                return visitor.visitChildren(self)




    def declaratorid(self):

        localctx = CPP14Parser.DeclaratoridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_declaratorid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1828
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Ellipsis:
                self.state = 1827
                self.match(CPP14Parser.Ellipsis)


            self.state = 1830
            self.idexpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierseqContext,0)


        def abstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.AbstractdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_typeid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeid" ):
                listener.enterTypeid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeid" ):
                listener.exitTypeid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeid" ):
                return visitor.visitTypeid(self)
            else:
                return visitor.visitChildren(self)




    def typeid(self):

        localctx = CPP14Parser.TypeidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_typeid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1832
            self.typespecifierseq()
            self.state = 1834
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,201,self._ctx)
            if la_ == 1:
                self.state = 1833
                self.abstractdeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AbstractdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ptrabstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.PtrabstractdeclaratorContext,0)


        def parametersandqualifiers(self):
            return self.getTypedRuleContext(CPP14Parser.ParametersandqualifiersContext,0)


        def trailingreturntype(self):
            return self.getTypedRuleContext(CPP14Parser.TrailingreturntypeContext,0)


        def noptrabstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrabstractdeclaratorContext,0)


        def abstractpackdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.AbstractpackdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_abstractdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstractdeclarator" ):
                listener.enterAbstractdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstractdeclarator" ):
                listener.exitAbstractdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstractdeclarator" ):
                return visitor.visitAbstractdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def abstractdeclarator(self):

        localctx = CPP14Parser.AbstractdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_abstractdeclarator)
        try:
            self.state = 1844
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,203,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1836
                self.ptrabstractdeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1838
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,202,self._ctx)
                if la_ == 1:
                    self.state = 1837
                    self.noptrabstractdeclarator(0)


                self.state = 1840
                self.parametersandqualifiers()
                self.state = 1841
                self.trailingreturntype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1843
                self.abstractpackdeclarator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PtrabstractdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noptrabstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrabstractdeclaratorContext,0)


        def ptroperator(self):
            return self.getTypedRuleContext(CPP14Parser.PtroperatorContext,0)


        def ptrabstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.PtrabstractdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_ptrabstractdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtrabstractdeclarator" ):
                listener.enterPtrabstractdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtrabstractdeclarator" ):
                listener.exitPtrabstractdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPtrabstractdeclarator" ):
                return visitor.visitPtrabstractdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def ptrabstractdeclarator(self):

        localctx = CPP14Parser.PtrabstractdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_ptrabstractdeclarator)
        try:
            self.state = 1851
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.LeftParen, CPP14Parser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1846
                self.noptrabstractdeclarator(0)
                pass
            elif token in [CPP14Parser.Decltype, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.AndAnd, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1847
                self.ptroperator()
                self.state = 1849
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,204,self._ctx)
                if la_ == 1:
                    self.state = 1848
                    self.ptrabstractdeclarator()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoptrabstractdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametersandqualifiers(self):
            return self.getTypedRuleContext(CPP14Parser.ParametersandqualifiersContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def ptrabstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.PtrabstractdeclaratorContext,0)


        def noptrabstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrabstractdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_noptrabstractdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoptrabstractdeclarator" ):
                listener.enterNoptrabstractdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoptrabstractdeclarator" ):
                listener.exitNoptrabstractdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoptrabstractdeclarator" ):
                return visitor.visitNoptrabstractdeclarator(self)
            else:
                return visitor.visitChildren(self)



    def noptrabstractdeclarator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.NoptrabstractdeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 274
        self.enterRecursionRule(localctx, 274, self.RULE_noptrabstractdeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1867
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,208,self._ctx)
            if la_ == 1:
                self.state = 1854
                self.parametersandqualifiers()
                pass

            elif la_ == 2:
                self.state = 1855
                self.match(CPP14Parser.LeftBracket)
                self.state = 1857
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 1856
                    self.constantexpression()


                self.state = 1859
                self.match(CPP14Parser.RightBracket)
                self.state = 1861
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,207,self._ctx)
                if la_ == 1:
                    self.state = 1860
                    self.attributespecifierseq(0)


                pass

            elif la_ == 3:
                self.state = 1863
                self.match(CPP14Parser.LeftParen)
                self.state = 1864
                self.ptrabstractdeclarator()
                self.state = 1865
                self.match(CPP14Parser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1882
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,212,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1880
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,211,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.NoptrabstractdeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrabstractdeclarator)
                        self.state = 1869
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 1870
                        self.parametersandqualifiers()
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.NoptrabstractdeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrabstractdeclarator)
                        self.state = 1871
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1872
                        self.match(CPP14Parser.LeftBracket)
                        self.state = 1874
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                            self.state = 1873
                            self.constantexpression()


                        self.state = 1876
                        self.match(CPP14Parser.RightBracket)
                        self.state = 1878
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,210,self._ctx)
                        if la_ == 1:
                            self.state = 1877
                            self.attributespecifierseq(0)


                        pass

             
                self.state = 1884
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,212,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AbstractpackdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noptrabstractpackdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrabstractpackdeclaratorContext,0)


        def ptroperator(self):
            return self.getTypedRuleContext(CPP14Parser.PtroperatorContext,0)


        def abstractpackdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.AbstractpackdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_abstractpackdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbstractpackdeclarator" ):
                listener.enterAbstractpackdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbstractpackdeclarator" ):
                listener.exitAbstractpackdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstractpackdeclarator" ):
                return visitor.visitAbstractpackdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def abstractpackdeclarator(self):

        localctx = CPP14Parser.AbstractpackdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_abstractpackdeclarator)
        try:
            self.state = 1889
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Ellipsis]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1885
                self.noptrabstractpackdeclarator(0)
                pass
            elif token in [CPP14Parser.Decltype, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.AndAnd, CPP14Parser.Doublecolon, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1886
                self.ptroperator()
                self.state = 1887
                self.abstractpackdeclarator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NoptrabstractpackdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noptrabstractpackdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.NoptrabstractpackdeclaratorContext,0)


        def parametersandqualifiers(self):
            return self.getTypedRuleContext(CPP14Parser.ParametersandqualifiersContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_noptrabstractpackdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoptrabstractpackdeclarator" ):
                listener.enterNoptrabstractpackdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoptrabstractpackdeclarator" ):
                listener.exitNoptrabstractpackdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoptrabstractpackdeclarator" ):
                return visitor.visitNoptrabstractpackdeclarator(self)
            else:
                return visitor.visitChildren(self)



    def noptrabstractpackdeclarator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.NoptrabstractpackdeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 278
        self.enterRecursionRule(localctx, 278, self.RULE_noptrabstractpackdeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1892
            self.match(CPP14Parser.Ellipsis)
            self._ctx.stop = self._input.LT(-1)
            self.state = 1907
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,217,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 1905
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,216,self._ctx)
                    if la_ == 1:
                        localctx = CPP14Parser.NoptrabstractpackdeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrabstractpackdeclarator)
                        self.state = 1894
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 1895
                        self.parametersandqualifiers()
                        pass

                    elif la_ == 2:
                        localctx = CPP14Parser.NoptrabstractpackdeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noptrabstractpackdeclarator)
                        self.state = 1896
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 1897
                        self.match(CPP14Parser.LeftBracket)
                        self.state = 1899
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                            self.state = 1898
                            self.constantexpression()


                        self.state = 1901
                        self.match(CPP14Parser.RightBracket)
                        self.state = 1903
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,215,self._ctx)
                        if la_ == 1:
                            self.state = 1902
                            self.attributespecifierseq(0)


                        pass

             
                self.state = 1909
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,217,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParameterdeclarationclauseContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterdeclarationlist(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterdeclarationlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_parameterdeclarationclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterdeclarationclause" ):
                listener.enterParameterdeclarationclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterdeclarationclause" ):
                listener.exitParameterdeclarationclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterdeclarationclause" ):
                return visitor.visitParameterdeclarationclause(self)
            else:
                return visitor.visitChildren(self)




    def parameterdeclarationclause(self):

        localctx = CPP14Parser.ParameterdeclarationclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_parameterdeclarationclause)
        self._la = 0 # Token type
        try:
            self.state = 1920
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,220,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1911
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Struct))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                    self.state = 1910
                    self.parameterdeclarationlist(0)


                self.state = 1914
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Ellipsis:
                    self.state = 1913
                    self.match(CPP14Parser.Ellipsis)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1916
                self.parameterdeclarationlist(0)
                self.state = 1917
                self.match(CPP14Parser.Comma)
                self.state = 1918
                self.match(CPP14Parser.Ellipsis)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterdeclarationlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterdeclarationContext,0)


        def parameterdeclarationlist(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterdeclarationlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_parameterdeclarationlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterdeclarationlist" ):
                listener.enterParameterdeclarationlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterdeclarationlist" ):
                listener.exitParameterdeclarationlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterdeclarationlist" ):
                return visitor.visitParameterdeclarationlist(self)
            else:
                return visitor.visitChildren(self)



    def parameterdeclarationlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.ParameterdeclarationlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 282
        self.enterRecursionRule(localctx, 282, self.RULE_parameterdeclarationlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1923
            self.parameterdeclaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 1930
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,221,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.ParameterdeclarationlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterdeclarationlist)
                    self.state = 1925
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 1926
                    self.match(CPP14Parser.Comma)
                    self.state = 1927
                    self.parameterdeclaration() 
                self.state = 1932
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,221,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParameterdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def initializerclause(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerclauseContext,0)


        def abstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.AbstractdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_parameterdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterdeclaration" ):
                listener.enterParameterdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterdeclaration" ):
                listener.exitParameterdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterdeclaration" ):
                return visitor.visitParameterdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def parameterdeclaration(self):

        localctx = CPP14Parser.ParameterdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_parameterdeclaration)
        self._la = 0 # Token type
        try:
            self.state = 1964
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,228,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1934
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1933
                    self.attributespecifierseq(0)


                self.state = 1936
                self.declspecifierseq()
                self.state = 1937
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1940
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1939
                    self.attributespecifierseq(0)


                self.state = 1942
                self.declspecifierseq()
                self.state = 1943
                self.declarator()
                self.state = 1944
                self.match(CPP14Parser.Assign)
                self.state = 1945
                self.initializerclause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1948
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1947
                    self.attributespecifierseq(0)


                self.state = 1950
                self.declspecifierseq()
                self.state = 1952
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,225,self._ctx)
                if la_ == 1:
                    self.state = 1951
                    self.abstractdeclarator()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1955
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 1954
                    self.attributespecifierseq(0)


                self.state = 1957
                self.declspecifierseq()
                self.state = 1959
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Decltype or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (CPP14Parser.LeftParen - 80)) | (1 << (CPP14Parser.LeftBracket - 80)) | (1 << (CPP14Parser.Star - 80)) | (1 << (CPP14Parser.And - 80)) | (1 << (CPP14Parser.AndAnd - 80)) | (1 << (CPP14Parser.Doublecolon - 80)) | (1 << (CPP14Parser.Ellipsis - 80)) | (1 << (CPP14Parser.Identifier - 80)))) != 0):
                    self.state = 1958
                    self.abstractdeclarator()


                self.state = 1961
                self.match(CPP14Parser.Assign)
                self.state = 1962
                self.initializerclause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctiondefinitionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(CPP14Parser.FunctionbodyContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def virtspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.VirtspecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_functiondefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctiondefinition" ):
                listener.enterFunctiondefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctiondefinition" ):
                listener.exitFunctiondefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctiondefinition" ):
                return visitor.visitFunctiondefinition(self)
            else:
                return visitor.visitChildren(self)




    def functiondefinition(self):

        localctx = CPP14Parser.FunctiondefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_functiondefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1967
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 1966
                self.attributespecifierseq(0)


            self.state = 1970
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,230,self._ctx)
            if la_ == 1:
                self.state = 1969
                self.declspecifierseq()


            self.state = 1972
            self.declarator()
            self.state = 1974
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Final or _la==CPP14Parser.Override:
                self.state = 1973
                self.virtspecifierseq(0)


            self.state = 1976
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionbodyContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.CompoundstatementContext,0)


        def ctorinitializer(self):
            return self.getTypedRuleContext(CPP14Parser.CtorinitializerContext,0)


        def functiontryblock(self):
            return self.getTypedRuleContext(CPP14Parser.FunctiontryblockContext,0)


        def Default(self):
            return self.getToken(CPP14Parser.Default, 0)

        def Delete(self):
            return self.getToken(CPP14Parser.Delete, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_functionbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionbody" ):
                listener.enterFunctionbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionbody" ):
                listener.exitFunctionbody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionbody" ):
                return visitor.visitFunctionbody(self)
            else:
                return visitor.visitChildren(self)




    def functionbody(self):

        localctx = CPP14Parser.FunctionbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_functionbody)
        self._la = 0 # Token type
        try:
            self.state = 1989
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,233,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1979
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Colon:
                    self.state = 1978
                    self.ctorinitializer()


                self.state = 1981
                self.compoundstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1982
                self.functiontryblock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1983
                self.match(CPP14Parser.Assign)
                self.state = 1984
                self.match(CPP14Parser.Default)
                self.state = 1985
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1986
                self.match(CPP14Parser.Assign)
                self.state = 1987
                self.match(CPP14Parser.Delete)
                self.state = 1988
                self.match(CPP14Parser.Semi)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CoroutinedefinitionContext(PrettyPrintParserRuleContext):
        def getText(self):
            COROUTINE_RETURN_TYPE = self.getDirtyText([0])
            COROUTINE_PARAMS = self.getDirtyText([1,0,0,1,1])
            COROUTINE_BODY = self.getDirtyText([2,0,1])
            COROUTINE_NAME = self.getDirtyText([1,0,0,0])
            ret = re.sub(r'___COROUTINE_RETURN_TYPE___', COROUTINE_RETURN_TYPE, REPLACE)
            ret = re.sub(r'___COROUTINE_PARAMS___', COROUTINE_PARAMS, ret)
            ret = re.sub(r'___COROUTINE_BODY___', COROUTINE_BODY, ret)
            ret = re.sub(r'___COROUTINE_NAME___', COROUTINE_NAME, ret)
            return ret

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def coroutinebody(self):
            return self.getTypedRuleContext(CPP14Parser.CoroutinebodyContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def virtspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.VirtspecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_coroutinedefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoroutinedefinition" ):
                listener.enterCoroutinedefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoroutinedefinition" ):
                listener.exitCoroutinedefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoroutinedefinition" ):
                return visitor.visitCoroutinedefinition(self)
            else:
                return visitor.visitChildren(self)




    def coroutinedefinition(self):

        localctx = CPP14Parser.CoroutinedefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_coroutinedefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1992
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                self.state = 1991
                self.attributespecifierseq(0)


            self.state = 1995
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,235,self._ctx)
            if la_ == 1:
                self.state = 1994
                self.declspecifierseq()


            self.state = 1997
            self.declarator()
            self.state = 1999
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Final or _la==CPP14Parser.Override:
                self.state = 1998
                self.virtspecifierseq(0)


            self.state = 2001
            self.coroutinebody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CoroutinebodyContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def co_compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.Co_compoundstatementContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_coroutinebody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoroutinebody" ):
                listener.enterCoroutinebody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoroutinebody" ):
                listener.exitCoroutinebody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoroutinebody" ):
                return visitor.visitCoroutinebody(self)
            else:
                return visitor.visitChildren(self)




    def coroutinebody(self):

        localctx = CPP14Parser.CoroutinebodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_coroutinebody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2003
            self.co_compoundstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def braceorequalinitializer(self):
            return self.getTypedRuleContext(CPP14Parser.BraceorequalinitializerContext,0)


        def expressionlist(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer" ):
                listener.enterInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer" ):
                listener.exitInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer" ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = CPP14Parser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_initializer)
        try:
            self.state = 2010
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.LeftBrace, CPP14Parser.Assign]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2005
                self.braceorequalinitializer()
                pass
            elif token in [CPP14Parser.LeftParen]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2006
                self.match(CPP14Parser.LeftParen)
                self.state = 2007
                self.expressionlist()
                self.state = 2008
                self.match(CPP14Parser.RightParen)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BraceorequalinitializerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializerclause(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerclauseContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_braceorequalinitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBraceorequalinitializer" ):
                listener.enterBraceorequalinitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBraceorequalinitializer" ):
                listener.exitBraceorequalinitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBraceorequalinitializer" ):
                return visitor.visitBraceorequalinitializer(self)
            else:
                return visitor.visitChildren(self)




    def braceorequalinitializer(self):

        localctx = CPP14Parser.BraceorequalinitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_braceorequalinitializer)
        try:
            self.state = 2015
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Assign]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2012
                self.match(CPP14Parser.Assign)
                self.state = 2013
                self.initializerclause()
                pass
            elif token in [CPP14Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2014
                self.bracedinitlist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerclauseContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentexpressionContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_initializerclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializerclause" ):
                listener.enterInitializerclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializerclause" ):
                listener.exitInitializerclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerclause" ):
                return visitor.visitInitializerclause(self)
            else:
                return visitor.visitChildren(self)




    def initializerclause(self):

        localctx = CPP14Parser.InitializerclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_initializerclause)
        try:
            self.state = 2019
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Alignof, CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Const_cast, CPP14Parser.Decltype, CPP14Parser.Delete, CPP14Parser.Double, CPP14Parser.Dynamic_cast, CPP14Parser.KFalse, CPP14Parser.Float, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.New, CPP14Parser.Noexcept, CPP14Parser.Nullptr, CPP14Parser.Operator, CPP14Parser.Reinterpret_cast, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Sizeof, CPP14Parser.Static_cast, CPP14Parser.This, CPP14Parser.Throw, CPP14Parser.KTrue, CPP14Parser.Typeid, CPP14Parser.Typename, CPP14Parser.Unsigned, CPP14Parser.Void, CPP14Parser.Wchar, CPP14Parser.LeftParen, CPP14Parser.LeftBracket, CPP14Parser.Plus, CPP14Parser.Minus, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.Or, CPP14Parser.Tilde, CPP14Parser.Not, CPP14Parser.PlusPlus, CPP14Parser.MinusMinus, CPP14Parser.Doublecolon, CPP14Parser.Identifier, CPP14Parser.Integerliteral, CPP14Parser.Characterliteral, CPP14Parser.Floatingliteral, CPP14Parser.Stringliteral, CPP14Parser.Userdefinedintegerliteral, CPP14Parser.Userdefinedfloatingliteral, CPP14Parser.Userdefinedstringliteral, CPP14Parser.Userdefinedcharacterliteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2017
                self.assignmentexpression()
                pass
            elif token in [CPP14Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2018
                self.bracedinitlist()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializerclause(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerclauseContext,0)


        def initializerlist(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_initializerlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializerlist" ):
                listener.enterInitializerlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializerlist" ):
                listener.exitInitializerlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerlist" ):
                return visitor.visitInitializerlist(self)
            else:
                return visitor.visitChildren(self)



    def initializerlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.InitializerlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 300
        self.enterRecursionRule(localctx, 300, self.RULE_initializerlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2022
            self.initializerclause()
            self.state = 2024
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,240,self._ctx)
            if la_ == 1:
                self.state = 2023
                self.match(CPP14Parser.Ellipsis)


            self._ctx.stop = self._input.LT(-1)
            self.state = 2034
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,242,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.InitializerlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerlist)
                    self.state = 2026
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2027
                    self.match(CPP14Parser.Comma)
                    self.state = 2028
                    self.initializerclause()
                    self.state = 2030
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,241,self._ctx)
                    if la_ == 1:
                        self.state = 2029
                        self.match(CPP14Parser.Ellipsis)

             
                self.state = 2036
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,242,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BracedinitlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializerlist(self):
            return self.getTypedRuleContext(CPP14Parser.InitializerlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_bracedinitlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracedinitlist" ):
                listener.enterBracedinitlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracedinitlist" ):
                listener.exitBracedinitlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracedinitlist" ):
                return visitor.visitBracedinitlist(self)
            else:
                return visitor.visitChildren(self)




    def bracedinitlist(self):

        localctx = CPP14Parser.BracedinitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_bracedinitlist)
        self._la = 0 # Token type
        try:
            self.state = 2046
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,244,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2037
                self.match(CPP14Parser.LeftBrace)
                self.state = 2038
                self.initializerlist(0)
                self.state = 2040
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Comma:
                    self.state = 2039
                    self.match(CPP14Parser.Comma)


                self.state = 2042
                self.match(CPP14Parser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2044
                self.match(CPP14Parser.LeftBrace)
                self.state = 2045
                self.match(CPP14Parser.RightBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassnameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_classname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassname" ):
                listener.enterClassname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassname" ):
                listener.exitClassname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassname" ):
                return visitor.visitClassname(self)
            else:
                return visitor.visitChildren(self)




    def classname(self):

        localctx = CPP14Parser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_classname)
        try:
            self.state = 2050
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,245,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2048
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2049
                self.simpletemplateid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classhead(self):
            return self.getTypedRuleContext(CPP14Parser.ClassheadContext,0)


        def memberspecification(self):
            return self.getTypedRuleContext(CPP14Parser.MemberspecificationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_classspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassspecifier" ):
                listener.enterClassspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassspecifier" ):
                listener.exitClassspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassspecifier" ):
                return visitor.visitClassspecifier(self)
            else:
                return visitor.visitChildren(self)




    def classspecifier(self):

        localctx = CPP14Parser.ClassspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_classspecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2052
            self.classhead()
            self.state = 2053
            self.match(CPP14Parser.LeftBrace)
            self.state = 2055
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Private) | (1 << CPP14Parser.Protected) | (1 << CPP14Parser.Public) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Template))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Using - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftParen - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Star - 65)) | (1 << (CPP14Parser.And - 65)) | (1 << (CPP14Parser.Tilde - 65)) | (1 << (CPP14Parser.AndAnd - 65)) | (1 << (CPP14Parser.Colon - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Semi - 65)) | (1 << (CPP14Parser.Ellipsis - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                self.state = 2054
                self.memberspecification()


            self.state = 2057
            self.match(CPP14Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassheadContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classkey(self):
            return self.getTypedRuleContext(CPP14Parser.ClasskeyContext,0)


        def classheadname(self):
            return self.getTypedRuleContext(CPP14Parser.ClassheadnameContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def classvirtspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.ClassvirtspecifierContext,0)


        def baseclause(self):
            return self.getTypedRuleContext(CPP14Parser.BaseclauseContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_classhead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasshead" ):
                listener.enterClasshead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasshead" ):
                listener.exitClasshead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasshead" ):
                return visitor.visitClasshead(self)
            else:
                return visitor.visitChildren(self)




    def classhead(self):

        localctx = CPP14Parser.ClassheadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_classhead)
        self._la = 0 # Token type
        try:
            self.state = 2077
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,252,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2059
                self.classkey()
                self.state = 2061
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2060
                    self.attributespecifierseq(0)


                self.state = 2063
                self.classheadname()
                self.state = 2065
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Final:
                    self.state = 2064
                    self.classvirtspecifier()


                self.state = 2068
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Colon:
                    self.state = 2067
                    self.baseclause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2070
                self.classkey()
                self.state = 2072
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2071
                    self.attributespecifierseq(0)


                self.state = 2075
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Colon:
                    self.state = 2074
                    self.baseclause()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassheadnameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(CPP14Parser.ClassnameContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_classheadname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassheadname" ):
                listener.enterClassheadname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassheadname" ):
                listener.exitClassheadname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassheadname" ):
                return visitor.visitClassheadname(self)
            else:
                return visitor.visitChildren(self)




    def classheadname(self):

        localctx = CPP14Parser.ClassheadnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_classheadname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2080
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,253,self._ctx)
            if la_ == 1:
                self.state = 2079
                self.nestednamespecifier(0)


            self.state = 2082
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassvirtspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Final(self):
            return self.getToken(CPP14Parser.Final, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_classvirtspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassvirtspecifier" ):
                listener.enterClassvirtspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassvirtspecifier" ):
                listener.exitClassvirtspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassvirtspecifier" ):
                return visitor.visitClassvirtspecifier(self)
            else:
                return visitor.visitChildren(self)




    def classvirtspecifier(self):

        localctx = CPP14Parser.ClassvirtspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_classvirtspecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2084
            self.match(CPP14Parser.Final)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClasskeyContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(CPP14Parser.Class, 0)

        def Struct(self):
            return self.getToken(CPP14Parser.Struct, 0)

        def Union(self):
            return self.getToken(CPP14Parser.Union, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_classkey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClasskey" ):
                listener.enterClasskey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClasskey" ):
                listener.exitClasskey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasskey" ):
                return visitor.visitClasskey(self)
            else:
                return visitor.visitChildren(self)




    def classkey(self):

        localctx = CPP14Parser.ClasskeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_classkey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2086
            _la = self._input.LA(1)
            if not(((((_la - 14)) & ~0x3f) == 0 and ((1 << (_la - 14)) & ((1 << (CPP14Parser.Class - 14)) | (1 << (CPP14Parser.Struct - 14)) | (1 << (CPP14Parser.Union - 14)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MemberspecificationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.MemberdeclarationContext,0)


        def memberspecification(self):
            return self.getTypedRuleContext(CPP14Parser.MemberspecificationContext,0)


        def accessspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.AccessspecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_memberspecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberspecification" ):
                listener.enterMemberspecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberspecification" ):
                listener.exitMemberspecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberspecification" ):
                return visitor.visitMemberspecification(self)
            else:
                return visitor.visitChildren(self)




    def memberspecification(self):

        localctx = CPP14Parser.MemberspecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_memberspecification)
        self._la = 0 # Token type
        try:
            self.state = 2097
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Alignas, CPP14Parser.Auto, CPP14Parser.Bool, CPP14Parser.Char, CPP14Parser.Char16, CPP14Parser.Char32, CPP14Parser.Class, CPP14Parser.Const, CPP14Parser.Constexpr, CPP14Parser.Decltype, CPP14Parser.Double, CPP14Parser.Enum, CPP14Parser.Explicit, CPP14Parser.Extern, CPP14Parser.Float, CPP14Parser.Friend, CPP14Parser.Inline, CPP14Parser.Int, CPP14Parser.Long, CPP14Parser.Mutable, CPP14Parser.Operator, CPP14Parser.Register, CPP14Parser.Short, CPP14Parser.Signed, CPP14Parser.Static, CPP14Parser.Static_assert, CPP14Parser.Struct, CPP14Parser.Template, CPP14Parser.Thread_local, CPP14Parser.Typedef, CPP14Parser.Typename, CPP14Parser.Union, CPP14Parser.Unsigned, CPP14Parser.Using, CPP14Parser.Virtual, CPP14Parser.Void, CPP14Parser.Volatile, CPP14Parser.Wchar, CPP14Parser.LeftParen, CPP14Parser.LeftBracket, CPP14Parser.Star, CPP14Parser.And, CPP14Parser.Tilde, CPP14Parser.AndAnd, CPP14Parser.Colon, CPP14Parser.Doublecolon, CPP14Parser.Semi, CPP14Parser.Ellipsis, CPP14Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2088
                self.memberdeclaration()
                self.state = 2090
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Private) | (1 << CPP14Parser.Protected) | (1 << CPP14Parser.Public) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Template))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Using - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftParen - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Star - 65)) | (1 << (CPP14Parser.And - 65)) | (1 << (CPP14Parser.Tilde - 65)) | (1 << (CPP14Parser.AndAnd - 65)) | (1 << (CPP14Parser.Colon - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Semi - 65)) | (1 << (CPP14Parser.Ellipsis - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                    self.state = 2089
                    self.memberspecification()


                pass
            elif token in [CPP14Parser.Private, CPP14Parser.Protected, CPP14Parser.Public]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2092
                self.accessspecifier()
                self.state = 2093
                self.match(CPP14Parser.Colon)
                self.state = 2095
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Constexpr) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Explicit) | (1 << CPP14Parser.Extern) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Friend) | (1 << CPP14Parser.Inline) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Mutable) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Private) | (1 << CPP14Parser.Protected) | (1 << CPP14Parser.Public) | (1 << CPP14Parser.Register) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Static) | (1 << CPP14Parser.Static_assert) | (1 << CPP14Parser.Struct) | (1 << CPP14Parser.Template))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CPP14Parser.Thread_local - 65)) | (1 << (CPP14Parser.Typedef - 65)) | (1 << (CPP14Parser.Typename - 65)) | (1 << (CPP14Parser.Union - 65)) | (1 << (CPP14Parser.Unsigned - 65)) | (1 << (CPP14Parser.Using - 65)) | (1 << (CPP14Parser.Virtual - 65)) | (1 << (CPP14Parser.Void - 65)) | (1 << (CPP14Parser.Volatile - 65)) | (1 << (CPP14Parser.Wchar - 65)) | (1 << (CPP14Parser.LeftParen - 65)) | (1 << (CPP14Parser.LeftBracket - 65)) | (1 << (CPP14Parser.Star - 65)) | (1 << (CPP14Parser.And - 65)) | (1 << (CPP14Parser.Tilde - 65)) | (1 << (CPP14Parser.AndAnd - 65)) | (1 << (CPP14Parser.Colon - 65)) | (1 << (CPP14Parser.Doublecolon - 65)) | (1 << (CPP14Parser.Semi - 65)) | (1 << (CPP14Parser.Ellipsis - 65)) | (1 << (CPP14Parser.Identifier - 65)))) != 0):
                    self.state = 2094
                    self.memberspecification()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MemberdeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def declspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.DeclspecifierseqContext,0)


        def memberdeclaratorlist(self):
            return self.getTypedRuleContext(CPP14Parser.MemberdeclaratorlistContext,0)


        def functiondefinition(self):
            return self.getTypedRuleContext(CPP14Parser.FunctiondefinitionContext,0)


        def usingdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.UsingdeclarationContext,0)


        def static_assertdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.Static_assertdeclarationContext,0)


        def templatedeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.TemplatedeclarationContext,0)


        def aliasdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.AliasdeclarationContext,0)


        def emptydeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.EmptydeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_memberdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberdeclaration" ):
                listener.enterMemberdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberdeclaration" ):
                listener.exitMemberdeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberdeclaration" ):
                return visitor.visitMemberdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def memberdeclaration(self):

        localctx = CPP14Parser.MemberdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_memberdeclaration)
        self._la = 0 # Token type
        try:
            self.state = 2115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,260,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,257,self._ctx)
                if la_ == 1:
                    self.state = 2099
                    self.attributespecifierseq(0)


                self.state = 2103
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,258,self._ctx)
                if la_ == 1:
                    self.state = 2102
                    self.declspecifierseq()


                self.state = 2106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignas) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Operator))) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (CPP14Parser.LeftParen - 80)) | (1 << (CPP14Parser.LeftBracket - 80)) | (1 << (CPP14Parser.Star - 80)) | (1 << (CPP14Parser.And - 80)) | (1 << (CPP14Parser.Tilde - 80)) | (1 << (CPP14Parser.AndAnd - 80)) | (1 << (CPP14Parser.Colon - 80)) | (1 << (CPP14Parser.Doublecolon - 80)) | (1 << (CPP14Parser.Ellipsis - 80)) | (1 << (CPP14Parser.Identifier - 80)))) != 0):
                    self.state = 2105
                    self.memberdeclaratorlist(0)


                self.state = 2108
                self.match(CPP14Parser.Semi)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2109
                self.functiondefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2110
                self.usingdeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2111
                self.static_assertdeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2112
                self.templatedeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2113
                self.aliasdeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2114
                self.emptydeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MemberdeclaratorlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.MemberdeclaratorContext,0)


        def memberdeclaratorlist(self):
            return self.getTypedRuleContext(CPP14Parser.MemberdeclaratorlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_memberdeclaratorlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberdeclaratorlist" ):
                listener.enterMemberdeclaratorlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberdeclaratorlist" ):
                listener.exitMemberdeclaratorlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberdeclaratorlist" ):
                return visitor.visitMemberdeclaratorlist(self)
            else:
                return visitor.visitChildren(self)



    def memberdeclaratorlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.MemberdeclaratorlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 320
        self.enterRecursionRule(localctx, 320, self.RULE_memberdeclaratorlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2118
            self.memberdeclarator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,261,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.MemberdeclaratorlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_memberdeclaratorlist)
                    self.state = 2120
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2121
                    self.match(CPP14Parser.Comma)
                    self.state = 2122
                    self.memberdeclarator() 
                self.state = 2127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,261,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MemberdeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def virtspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.VirtspecifierseqContext,0)


        def purespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.PurespecifierContext,0)


        def braceorequalinitializer(self):
            return self.getTypedRuleContext(CPP14Parser.BraceorequalinitializerContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_memberdeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberdeclarator" ):
                listener.enterMemberdeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberdeclarator" ):
                listener.exitMemberdeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberdeclarator" ):
                return visitor.visitMemberdeclarator(self)
            else:
                return visitor.visitChildren(self)




    def memberdeclarator(self):

        localctx = CPP14Parser.MemberdeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_memberdeclarator)
        self._la = 0 # Token type
        try:
            self.state = 2147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,267,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2128
                self.declarator()
                self.state = 2130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,262,self._ctx)
                if la_ == 1:
                    self.state = 2129
                    self.virtspecifierseq(0)


                self.state = 2133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,263,self._ctx)
                if la_ == 1:
                    self.state = 2132
                    self.purespecifier()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2135
                self.declarator()
                self.state = 2137
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,264,self._ctx)
                if la_ == 1:
                    self.state = 2136
                    self.braceorequalinitializer()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Identifier:
                    self.state = 2139
                    self.match(CPP14Parser.Identifier)


                self.state = 2143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2142
                    self.attributespecifierseq(0)


                self.state = 2145
                self.match(CPP14Parser.Colon)
                self.state = 2146
                self.constantexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VirtspecifierseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def virtspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.VirtspecifierContext,0)


        def virtspecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.VirtspecifierseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_virtspecifierseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVirtspecifierseq" ):
                listener.enterVirtspecifierseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVirtspecifierseq" ):
                listener.exitVirtspecifierseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVirtspecifierseq" ):
                return visitor.visitVirtspecifierseq(self)
            else:
                return visitor.visitChildren(self)



    def virtspecifierseq(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.VirtspecifierseqContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 324
        self.enterRecursionRule(localctx, 324, self.RULE_virtspecifierseq, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2150
            self.virtspecifier()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,268,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.VirtspecifierseqContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_virtspecifierseq)
                    self.state = 2152
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2153
                    self.virtspecifier() 
                self.state = 2158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,268,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class VirtspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Override(self):
            return self.getToken(CPP14Parser.Override, 0)

        def Final(self):
            return self.getToken(CPP14Parser.Final, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_virtspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVirtspecifier" ):
                listener.enterVirtspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVirtspecifier" ):
                listener.exitVirtspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVirtspecifier" ):
                return visitor.visitVirtspecifier(self)
            else:
                return visitor.visitChildren(self)




    def virtspecifier(self):

        localctx = CPP14Parser.VirtspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_virtspecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2159
            _la = self._input.LA(1)
            if not(_la==CPP14Parser.Final or _la==CPP14Parser.Override):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PurespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None # Token

        def Assign(self):
            return self.getToken(CPP14Parser.Assign, 0)

        def Octalliteral(self):
            return self.getToken(CPP14Parser.Octalliteral, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_purespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPurespecifier" ):
                listener.enterPurespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPurespecifier" ):
                listener.exitPurespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPurespecifier" ):
                return visitor.visitPurespecifier(self)
            else:
                return visitor.visitChildren(self)




    def purespecifier(self):

        localctx = CPP14Parser.PurespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_purespecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2161
            self.match(CPP14Parser.Assign)
            self.state = 2162
            localctx.val = self.match(CPP14Parser.Octalliteral)
#            if((None if localctx.val is None else localctx.val.text).compareTo("0")!=0) throw new InputMismatchException(this);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BaseclauseContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basespecifierlist(self):
            return self.getTypedRuleContext(CPP14Parser.BasespecifierlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_baseclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseclause" ):
                listener.enterBaseclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseclause" ):
                listener.exitBaseclause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseclause" ):
                return visitor.visitBaseclause(self)
            else:
                return visitor.visitChildren(self)




    def baseclause(self):

        localctx = CPP14Parser.BaseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_baseclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2165
            self.match(CPP14Parser.Colon)
            self.state = 2166
            self.basespecifierlist(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BasespecifierlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.BasespecifierContext,0)


        def basespecifierlist(self):
            return self.getTypedRuleContext(CPP14Parser.BasespecifierlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_basespecifierlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasespecifierlist" ):
                listener.enterBasespecifierlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasespecifierlist" ):
                listener.exitBasespecifierlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasespecifierlist" ):
                return visitor.visitBasespecifierlist(self)
            else:
                return visitor.visitChildren(self)



    def basespecifierlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.BasespecifierlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 332
        self.enterRecursionRule(localctx, 332, self.RULE_basespecifierlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2169
            self.basespecifier()
            self.state = 2171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,269,self._ctx)
            if la_ == 1:
                self.state = 2170
                self.match(CPP14Parser.Ellipsis)


            self._ctx.stop = self._input.LT(-1)
            self.state = 2181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,271,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.BasespecifierlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_basespecifierlist)
                    self.state = 2173
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2174
                    self.match(CPP14Parser.Comma)
                    self.state = 2175
                    self.basespecifier()
                    self.state = 2177
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,270,self._ctx)
                    if la_ == 1:
                        self.state = 2176
                        self.match(CPP14Parser.Ellipsis)

             
                self.state = 2183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,271,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BasespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basetypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.BasetypespecifierContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def Virtual(self):
            return self.getToken(CPP14Parser.Virtual, 0)

        def accessspecifier(self):
            return self.getTypedRuleContext(CPP14Parser.AccessspecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_basespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasespecifier" ):
                listener.enterBasespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasespecifier" ):
                listener.exitBasespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasespecifier" ):
                return visitor.visitBasespecifier(self)
            else:
                return visitor.visitChildren(self)




    def basespecifier(self):

        localctx = CPP14Parser.BasespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_basespecifier)
        self._la = 0 # Token type
        try:
            self.state = 2205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,277,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2184
                    self.attributespecifierseq(0)


                self.state = 2187
                self.basetypespecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2188
                    self.attributespecifierseq(0)


                self.state = 2191
                self.match(CPP14Parser.Virtual)
                self.state = 2193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Private) | (1 << CPP14Parser.Protected) | (1 << CPP14Parser.Public))) != 0):
                    self.state = 2192
                    self.accessspecifier()


                self.state = 2195
                self.basetypespecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2196
                    self.attributespecifierseq(0)


                self.state = 2199
                self.accessspecifier()
                self.state = 2201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Virtual:
                    self.state = 2200
                    self.match(CPP14Parser.Virtual)


                self.state = 2203
                self.basetypespecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassordecltypeContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(CPP14Parser.ClassnameContext,0)


        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def decltypespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.DecltypespecifierContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_classordecltype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassordecltype" ):
                listener.enterClassordecltype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassordecltype" ):
                listener.exitClassordecltype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassordecltype" ):
                return visitor.visitClassordecltype(self)
            else:
                return visitor.visitChildren(self)




    def classordecltype(self):

        localctx = CPP14Parser.ClassordecltypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_classordecltype)
        try:
            self.state = 2212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,279,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2208
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,278,self._ctx)
                if la_ == 1:
                    self.state = 2207
                    self.nestednamespecifier(0)


                self.state = 2210
                self.classname()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2211
                self.decltypespecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BasetypespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classordecltype(self):
            return self.getTypedRuleContext(CPP14Parser.ClassordecltypeContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_basetypespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasetypespecifier" ):
                listener.enterBasetypespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasetypespecifier" ):
                listener.exitBasetypespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasetypespecifier" ):
                return visitor.visitBasetypespecifier(self)
            else:
                return visitor.visitChildren(self)




    def basetypespecifier(self):

        localctx = CPP14Parser.BasetypespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_basetypespecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2214
            self.classordecltype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AccessspecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Private(self):
            return self.getToken(CPP14Parser.Private, 0)

        def Protected(self):
            return self.getToken(CPP14Parser.Protected, 0)

        def Public(self):
            return self.getToken(CPP14Parser.Public, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_accessspecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessspecifier" ):
                listener.enterAccessspecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessspecifier" ):
                listener.exitAccessspecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessspecifier" ):
                return visitor.visitAccessspecifier(self)
            else:
                return visitor.visitChildren(self)




    def accessspecifier(self):

        localctx = CPP14Parser.AccessspecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_accessspecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2216
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Private) | (1 << CPP14Parser.Protected) | (1 << CPP14Parser.Public))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConversionfunctionidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Operator(self):
            return self.getToken(CPP14Parser.Operator, 0)

        def conversiontypeid(self):
            return self.getTypedRuleContext(CPP14Parser.ConversiontypeidContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_conversionfunctionid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversionfunctionid" ):
                listener.enterConversionfunctionid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversionfunctionid" ):
                listener.exitConversionfunctionid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversionfunctionid" ):
                return visitor.visitConversionfunctionid(self)
            else:
                return visitor.visitChildren(self)




    def conversionfunctionid(self):

        localctx = CPP14Parser.ConversionfunctionidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_conversionfunctionid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2218
            self.match(CPP14Parser.Operator)
            self.state = 2219
            self.conversiontypeid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConversiontypeidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierseqContext,0)


        def conversiondeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.ConversiondeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_conversiontypeid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversiontypeid" ):
                listener.enterConversiontypeid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversiontypeid" ):
                listener.exitConversiontypeid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversiontypeid" ):
                return visitor.visitConversiontypeid(self)
            else:
                return visitor.visitChildren(self)




    def conversiontypeid(self):

        localctx = CPP14Parser.ConversiontypeidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_conversiontypeid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2221
            self.typespecifierseq()
            self.state = 2223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,280,self._ctx)
            if la_ == 1:
                self.state = 2222
                self.conversiondeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConversiondeclaratorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ptroperator(self):
            return self.getTypedRuleContext(CPP14Parser.PtroperatorContext,0)


        def conversiondeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.ConversiondeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_conversiondeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConversiondeclarator" ):
                listener.enterConversiondeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConversiondeclarator" ):
                listener.exitConversiondeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversiondeclarator" ):
                return visitor.visitConversiondeclarator(self)
            else:
                return visitor.visitChildren(self)




    def conversiondeclarator(self):

        localctx = CPP14Parser.ConversiondeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_conversiondeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2225
            self.ptroperator()
            self.state = 2227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,281,self._ctx)
            if la_ == 1:
                self.state = 2226
                self.conversiondeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CtorinitializerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meminitializerlist(self):
            return self.getTypedRuleContext(CPP14Parser.MeminitializerlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_ctorinitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtorinitializer" ):
                listener.enterCtorinitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtorinitializer" ):
                listener.exitCtorinitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCtorinitializer" ):
                return visitor.visitCtorinitializer(self)
            else:
                return visitor.visitChildren(self)




    def ctorinitializer(self):

        localctx = CPP14Parser.CtorinitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_ctorinitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2229
            self.match(CPP14Parser.Colon)
            self.state = 2230
            self.meminitializerlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MeminitializerlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meminitializer(self):
            return self.getTypedRuleContext(CPP14Parser.MeminitializerContext,0)


        def meminitializerlist(self):
            return self.getTypedRuleContext(CPP14Parser.MeminitializerlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_meminitializerlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeminitializerlist" ):
                listener.enterMeminitializerlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeminitializerlist" ):
                listener.exitMeminitializerlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeminitializerlist" ):
                return visitor.visitMeminitializerlist(self)
            else:
                return visitor.visitChildren(self)




    def meminitializerlist(self):

        localctx = CPP14Parser.MeminitializerlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_meminitializerlist)
        self._la = 0 # Token type
        try:
            self.state = 2243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,284,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2232
                self.meminitializer()
                self.state = 2234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Ellipsis:
                    self.state = 2233
                    self.match(CPP14Parser.Ellipsis)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2236
                self.meminitializer()
                self.state = 2238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Ellipsis:
                    self.state = 2237
                    self.match(CPP14Parser.Ellipsis)


                self.state = 2240
                self.match(CPP14Parser.Comma)
                self.state = 2241
                self.meminitializerlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MeminitializerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def meminitializerid(self):
            return self.getTypedRuleContext(CPP14Parser.MeminitializeridContext,0)


        def expressionlist(self):
            return self.getTypedRuleContext(CPP14Parser.ExpressionlistContext,0)


        def bracedinitlist(self):
            return self.getTypedRuleContext(CPP14Parser.BracedinitlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_meminitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeminitializer" ):
                listener.enterMeminitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeminitializer" ):
                listener.exitMeminitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeminitializer" ):
                return visitor.visitMeminitializer(self)
            else:
                return visitor.visitChildren(self)




    def meminitializer(self):

        localctx = CPP14Parser.MeminitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_meminitializer)
        self._la = 0 # Token type
        try:
            self.state = 2255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,286,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2245
                self.meminitializerid()
                self.state = 2246
                self.match(CPP14Parser.LeftParen)
                self.state = 2248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.Throw - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.LeftBrace - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 2247
                    self.expressionlist()


                self.state = 2250
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2252
                self.meminitializerid()
                self.state = 2253
                self.bracedinitlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MeminitializeridContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classordecltype(self):
            return self.getTypedRuleContext(CPP14Parser.ClassordecltypeContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_meminitializerid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeminitializerid" ):
                listener.enterMeminitializerid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeminitializerid" ):
                listener.exitMeminitializerid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeminitializerid" ):
                return visitor.visitMeminitializerid(self)
            else:
                return visitor.visitChildren(self)




    def meminitializerid(self):

        localctx = CPP14Parser.MeminitializeridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_meminitializerid)
        try:
            self.state = 2259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,287,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2257
                self.classordecltype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2258
                self.match(CPP14Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorfunctionidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Operator(self):
            return self.getToken(CPP14Parser.Operator, 0)

        def operator(self):
            return self.getTypedRuleContext(CPP14Parser.OperatorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_operatorfunctionid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorfunctionid" ):
                listener.enterOperatorfunctionid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorfunctionid" ):
                listener.exitOperatorfunctionid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorfunctionid" ):
                return visitor.visitOperatorfunctionid(self)
            else:
                return visitor.visitChildren(self)




    def operatorfunctionid(self):

        localctx = CPP14Parser.OperatorfunctionidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_operatorfunctionid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2261
            self.match(CPP14Parser.Operator)
            self.state = 2262
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteraloperatoridContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Operator(self):
            return self.getToken(CPP14Parser.Operator, 0)

        def Stringliteral(self):
            return self.getToken(CPP14Parser.Stringliteral, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def Userdefinedstringliteral(self):
            return self.getToken(CPP14Parser.Userdefinedstringliteral, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_literaloperatorid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteraloperatorid" ):
                listener.enterLiteraloperatorid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteraloperatorid" ):
                listener.exitLiteraloperatorid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteraloperatorid" ):
                return visitor.visitLiteraloperatorid(self)
            else:
                return visitor.visitChildren(self)




    def literaloperatorid(self):

        localctx = CPP14Parser.LiteraloperatoridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_literaloperatorid)
        try:
            self.state = 2269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,288,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2264
                self.match(CPP14Parser.Operator)
                self.state = 2265
                self.match(CPP14Parser.Stringliteral)
                self.state = 2266
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2267
                self.match(CPP14Parser.Operator)
                self.state = 2268
                self.match(CPP14Parser.Userdefinedstringliteral)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TemplatedeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def templateparameterlist(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateparameterlistContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_templatedeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplatedeclaration" ):
                listener.enterTemplatedeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplatedeclaration" ):
                listener.exitTemplatedeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplatedeclaration" ):
                return visitor.visitTemplatedeclaration(self)
            else:
                return visitor.visitChildren(self)




    def templatedeclaration(self):

        localctx = CPP14Parser.TemplatedeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_templatedeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2271
            self.match(CPP14Parser.Template)
            self.state = 2272
            self.match(CPP14Parser.Less)
            self.state = 2273
            self.templateparameterlist(0)
            self.state = 2274
            self.match(CPP14Parser.Greater)
            self.state = 2275
            self.declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TemplateparameterlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templateparameter(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateparameterContext,0)


        def templateparameterlist(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateparameterlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_templateparameterlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateparameterlist" ):
                listener.enterTemplateparameterlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateparameterlist" ):
                listener.exitTemplateparameterlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateparameterlist" ):
                return visitor.visitTemplateparameterlist(self)
            else:
                return visitor.visitChildren(self)



    def templateparameterlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.TemplateparameterlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 362
        self.enterRecursionRule(localctx, 362, self.RULE_templateparameterlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2278
            self.templateparameter()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,289,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.TemplateparameterlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_templateparameterlist)
                    self.state = 2280
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2281
                    self.match(CPP14Parser.Comma)
                    self.state = 2282
                    self.templateparameter() 
                self.state = 2287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,289,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TemplateparameterContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeparameter(self):
            return self.getTypedRuleContext(CPP14Parser.TypeparameterContext,0)


        def parameterdeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.ParameterdeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_templateparameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateparameter" ):
                listener.enterTemplateparameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateparameter" ):
                listener.exitTemplateparameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateparameter" ):
                return visitor.visitTemplateparameter(self)
            else:
                return visitor.visitChildren(self)




    def templateparameter(self):

        localctx = CPP14Parser.TemplateparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_templateparameter)
        try:
            self.state = 2290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,290,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2288
                self.typeparameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2289
                self.parameterdeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeparameterContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(CPP14Parser.Class, 0)

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def Typename(self):
            return self.getToken(CPP14Parser.Typename, 0)

        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def templateparameterlist(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateparameterlistContext,0)


        def idexpression(self):
            return self.getTypedRuleContext(CPP14Parser.IdexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_typeparameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeparameter" ):
                listener.enterTypeparameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeparameter" ):
                listener.exitTypeparameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeparameter" ):
                return visitor.visitTypeparameter(self)
            else:
                return visitor.visitChildren(self)




    def typeparameter(self):

        localctx = CPP14Parser.TypeparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_typeparameter)
        self._la = 0 # Token type
        try:
            self.state = 2340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,300,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2292
                self.match(CPP14Parser.Class)
                self.state = 2294
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,291,self._ctx)
                if la_ == 1:
                    self.state = 2293
                    self.match(CPP14Parser.Ellipsis)


                self.state = 2297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,292,self._ctx)
                if la_ == 1:
                    self.state = 2296
                    self.match(CPP14Parser.Identifier)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2299
                self.match(CPP14Parser.Class)
                self.state = 2301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Identifier:
                    self.state = 2300
                    self.match(CPP14Parser.Identifier)


                self.state = 2303
                self.match(CPP14Parser.Assign)
                self.state = 2304
                self.typeid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2305
                self.match(CPP14Parser.Typename)
                self.state = 2307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,294,self._ctx)
                if la_ == 1:
                    self.state = 2306
                    self.match(CPP14Parser.Ellipsis)


                self.state = 2310
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,295,self._ctx)
                if la_ == 1:
                    self.state = 2309
                    self.match(CPP14Parser.Identifier)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2312
                self.match(CPP14Parser.Typename)
                self.state = 2314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Identifier:
                    self.state = 2313
                    self.match(CPP14Parser.Identifier)


                self.state = 2316
                self.match(CPP14Parser.Assign)
                self.state = 2317
                self.typeid()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2318
                self.match(CPP14Parser.Template)
                self.state = 2319
                self.match(CPP14Parser.Less)
                self.state = 2320
                self.templateparameterlist(0)
                self.state = 2321
                self.match(CPP14Parser.Greater)
                self.state = 2322
                self.match(CPP14Parser.Class)
                self.state = 2324
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,297,self._ctx)
                if la_ == 1:
                    self.state = 2323
                    self.match(CPP14Parser.Ellipsis)


                self.state = 2327
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,298,self._ctx)
                if la_ == 1:
                    self.state = 2326
                    self.match(CPP14Parser.Identifier)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2329
                self.match(CPP14Parser.Template)
                self.state = 2330
                self.match(CPP14Parser.Less)
                self.state = 2331
                self.templateparameterlist(0)
                self.state = 2332
                self.match(CPP14Parser.Greater)
                self.state = 2333
                self.match(CPP14Parser.Class)
                self.state = 2335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Identifier:
                    self.state = 2334
                    self.match(CPP14Parser.Identifier)


                self.state = 2337
                self.match(CPP14Parser.Assign)
                self.state = 2338
                self.idexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpletemplateidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templatename(self):
            return self.getTypedRuleContext(CPP14Parser.TemplatenameContext,0)


        def templateargumentlist(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateargumentlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_simpletemplateid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpletemplateid" ):
                listener.enterSimpletemplateid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpletemplateid" ):
                listener.exitSimpletemplateid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpletemplateid" ):
                return visitor.visitSimpletemplateid(self)
            else:
                return visitor.visitChildren(self)




    def simpletemplateid(self):

        localctx = CPP14Parser.SimpletemplateidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_simpletemplateid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2342
            self.templatename()
            self.state = 2343
            self.match(CPP14Parser.Less)
            self.state = 2345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast) | (1 << CPP14Parser.Struct))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Union - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Volatile - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                self.state = 2344
                self.templateargumentlist(0)


            self.state = 2347
            self.match(CPP14Parser.Greater)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TemplateidContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def operatorfunctionid(self):
            return self.getTypedRuleContext(CPP14Parser.OperatorfunctionidContext,0)


        def templateargumentlist(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateargumentlistContext,0)


        def literaloperatorid(self):
            return self.getTypedRuleContext(CPP14Parser.LiteraloperatoridContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_templateid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateid" ):
                listener.enterTemplateid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateid" ):
                listener.exitTemplateid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateid" ):
                return visitor.visitTemplateid(self)
            else:
                return visitor.visitChildren(self)




    def templateid(self):

        localctx = CPP14Parser.TemplateidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_templateid)
        self._la = 0 # Token type
        try:
            self.state = 2364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,304,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2349
                self.simpletemplateid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2350
                self.operatorfunctionid()
                self.state = 2351
                self.match(CPP14Parser.Less)
                self.state = 2353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast) | (1 << CPP14Parser.Struct))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Union - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Volatile - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 2352
                    self.templateargumentlist(0)


                self.state = 2355
                self.match(CPP14Parser.Greater)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2357
                self.literaloperatorid()
                self.state = 2358
                self.match(CPP14Parser.Less)
                self.state = 2360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Alignof) | (1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Const_cast) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Delete) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Dynamic_cast) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.KFalse) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.New) | (1 << CPP14Parser.Noexcept) | (1 << CPP14Parser.Nullptr) | (1 << CPP14Parser.Operator) | (1 << CPP14Parser.Reinterpret_cast) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Sizeof) | (1 << CPP14Parser.Static_cast) | (1 << CPP14Parser.Struct))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CPP14Parser.This - 64)) | (1 << (CPP14Parser.KTrue - 64)) | (1 << (CPP14Parser.Typeid - 64)) | (1 << (CPP14Parser.Typename - 64)) | (1 << (CPP14Parser.Union - 64)) | (1 << (CPP14Parser.Unsigned - 64)) | (1 << (CPP14Parser.Void - 64)) | (1 << (CPP14Parser.Volatile - 64)) | (1 << (CPP14Parser.Wchar - 64)) | (1 << (CPP14Parser.LeftParen - 64)) | (1 << (CPP14Parser.LeftBracket - 64)) | (1 << (CPP14Parser.Plus - 64)) | (1 << (CPP14Parser.Minus - 64)) | (1 << (CPP14Parser.Star - 64)) | (1 << (CPP14Parser.And - 64)) | (1 << (CPP14Parser.Or - 64)) | (1 << (CPP14Parser.Tilde - 64)) | (1 << (CPP14Parser.Not - 64)) | (1 << (CPP14Parser.PlusPlus - 64)) | (1 << (CPP14Parser.MinusMinus - 64)) | (1 << (CPP14Parser.Doublecolon - 64)) | (1 << (CPP14Parser.Identifier - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (CPP14Parser.Integerliteral - 128)) | (1 << (CPP14Parser.Characterliteral - 128)) | (1 << (CPP14Parser.Floatingliteral - 128)) | (1 << (CPP14Parser.Stringliteral - 128)) | (1 << (CPP14Parser.Userdefinedintegerliteral - 128)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 128)) | (1 << (CPP14Parser.Userdefinedstringliteral - 128)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 128)))) != 0):
                    self.state = 2359
                    self.templateargumentlist(0)


                self.state = 2362
                self.match(CPP14Parser.Greater)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TemplatenameContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_templatename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplatename" ):
                listener.enterTemplatename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplatename" ):
                listener.exitTemplatename(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplatename" ):
                return visitor.visitTemplatename(self)
            else:
                return visitor.visitChildren(self)




    def templatename(self):

        localctx = CPP14Parser.TemplatenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_templatename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2366
            self.match(CPP14Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TemplateargumentlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templateargument(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateargumentContext,0)


        def templateargumentlist(self):
            return self.getTypedRuleContext(CPP14Parser.TemplateargumentlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_templateargumentlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateargumentlist" ):
                listener.enterTemplateargumentlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateargumentlist" ):
                listener.exitTemplateargumentlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateargumentlist" ):
                return visitor.visitTemplateargumentlist(self)
            else:
                return visitor.visitChildren(self)



    def templateargumentlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.TemplateargumentlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 374
        self.enterRecursionRule(localctx, 374, self.RULE_templateargumentlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2369
            self.templateargument()
            self.state = 2371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,305,self._ctx)
            if la_ == 1:
                self.state = 2370
                self.match(CPP14Parser.Ellipsis)


            self._ctx.stop = self._input.LT(-1)
            self.state = 2381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,307,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.TemplateargumentlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_templateargumentlist)
                    self.state = 2373
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2374
                    self.match(CPP14Parser.Comma)
                    self.state = 2375
                    self.templateargument()
                    self.state = 2377
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,306,self._ctx)
                    if la_ == 1:
                        self.state = 2376
                        self.match(CPP14Parser.Ellipsis)

             
                self.state = 2383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,307,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TemplateargumentContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def idexpression(self):
            return self.getTypedRuleContext(CPP14Parser.IdexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_templateargument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateargument" ):
                listener.enterTemplateargument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateargument" ):
                listener.exitTemplateargument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateargument" ):
                return visitor.visitTemplateargument(self)
            else:
                return visitor.visitChildren(self)




    def templateargument(self):

        localctx = CPP14Parser.TemplateargumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_templateargument)
        try:
            self.state = 2387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,308,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2384
                self.typeid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2385
                self.constantexpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2386
                self.idexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypenamespecifierContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Typename(self):
            return self.getToken(CPP14Parser.Typename, 0)

        def nestednamespecifier(self):
            return self.getTypedRuleContext(CPP14Parser.NestednamespecifierContext,0)


        def Identifier(self):
            return self.getToken(CPP14Parser.Identifier, 0)

        def simpletemplateid(self):
            return self.getTypedRuleContext(CPP14Parser.SimpletemplateidContext,0)


        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_typenamespecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypenamespecifier" ):
                listener.enterTypenamespecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypenamespecifier" ):
                listener.exitTypenamespecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypenamespecifier" ):
                return visitor.visitTypenamespecifier(self)
            else:
                return visitor.visitChildren(self)




    def typenamespecifier(self):

        localctx = CPP14Parser.TypenamespecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_typenamespecifier)
        self._la = 0 # Token type
        try:
            self.state = 2400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,310,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2389
                self.match(CPP14Parser.Typename)
                self.state = 2390
                self.nestednamespecifier(0)
                self.state = 2391
                self.match(CPP14Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2393
                self.match(CPP14Parser.Typename)
                self.state = 2394
                self.nestednamespecifier(0)
                self.state = 2396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Template:
                    self.state = 2395
                    self.match(CPP14Parser.Template)


                self.state = 2398
                self.simpletemplateid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExplicitinstantiationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def declaration(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationContext,0)


        def Extern(self):
            return self.getToken(CPP14Parser.Extern, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_explicitinstantiation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicitinstantiation" ):
                listener.enterExplicitinstantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicitinstantiation" ):
                listener.exitExplicitinstantiation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitinstantiation" ):
                return visitor.visitExplicitinstantiation(self)
            else:
                return visitor.visitChildren(self)




    def explicitinstantiation(self):

        localctx = CPP14Parser.ExplicitinstantiationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_explicitinstantiation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Extern:
                self.state = 2402
                self.match(CPP14Parser.Extern)


            self.state = 2405
            self.match(CPP14Parser.Template)
            self.state = 2406
            self.declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExplicitspecializationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Template(self):
            return self.getToken(CPP14Parser.Template, 0)

        def declaration(self):
            return self.getTypedRuleContext(CPP14Parser.DeclarationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_explicitspecialization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicitspecialization" ):
                listener.enterExplicitspecialization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicitspecialization" ):
                listener.exitExplicitspecialization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitspecialization" ):
                return visitor.visitExplicitspecialization(self)
            else:
                return visitor.visitChildren(self)




    def explicitspecialization(self):

        localctx = CPP14Parser.ExplicitspecializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_explicitspecialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2408
            self.match(CPP14Parser.Template)
            self.state = 2409
            self.match(CPP14Parser.Less)
            self.state = 2410
            self.match(CPP14Parser.Greater)
            self.state = 2411
            self.declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TryblockContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(CPP14Parser.Try, 0)

        def compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.CompoundstatementContext,0)


        def handlerseq(self):
            return self.getTypedRuleContext(CPP14Parser.HandlerseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_tryblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryblock" ):
                listener.enterTryblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryblock" ):
                listener.exitTryblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryblock" ):
                return visitor.visitTryblock(self)
            else:
                return visitor.visitChildren(self)




    def tryblock(self):

        localctx = CPP14Parser.TryblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_tryblock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2413
            self.match(CPP14Parser.Try)
            self.state = 2414
            self.compoundstatement()
            self.state = 2415
            self.handlerseq()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctiontryblockContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(CPP14Parser.Try, 0)

        def compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.CompoundstatementContext,0)


        def handlerseq(self):
            return self.getTypedRuleContext(CPP14Parser.HandlerseqContext,0)


        def ctorinitializer(self):
            return self.getTypedRuleContext(CPP14Parser.CtorinitializerContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_functiontryblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctiontryblock" ):
                listener.enterFunctiontryblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctiontryblock" ):
                listener.exitFunctiontryblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctiontryblock" ):
                return visitor.visitFunctiontryblock(self)
            else:
                return visitor.visitChildren(self)




    def functiontryblock(self):

        localctx = CPP14Parser.FunctiontryblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_functiontryblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2417
            self.match(CPP14Parser.Try)
            self.state = 2419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPP14Parser.Colon:
                self.state = 2418
                self.ctorinitializer()


            self.state = 2421
            self.compoundstatement()
            self.state = 2422
            self.handlerseq()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HandlerseqContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def handler(self):
            return self.getTypedRuleContext(CPP14Parser.HandlerContext,0)


        def handlerseq(self):
            return self.getTypedRuleContext(CPP14Parser.HandlerseqContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_handlerseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHandlerseq" ):
                listener.enterHandlerseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHandlerseq" ):
                listener.exitHandlerseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHandlerseq" ):
                return visitor.visitHandlerseq(self)
            else:
                return visitor.visitChildren(self)




    def handlerseq(self):

        localctx = CPP14Parser.HandlerseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_handlerseq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2424
            self.handler()
            self.state = 2426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,313,self._ctx)
            if la_ == 1:
                self.state = 2425
                self.handlerseq()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HandlerContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(CPP14Parser.Catch, 0)

        def exceptiondeclaration(self):
            return self.getTypedRuleContext(CPP14Parser.ExceptiondeclarationContext,0)


        def compoundstatement(self):
            return self.getTypedRuleContext(CPP14Parser.CompoundstatementContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_handler

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHandler" ):
                listener.enterHandler(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHandler" ):
                listener.exitHandler(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHandler" ):
                return visitor.visitHandler(self)
            else:
                return visitor.visitChildren(self)




    def handler(self):

        localctx = CPP14Parser.HandlerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_handler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2428
            self.match(CPP14Parser.Catch)
            self.state = 2429
            self.match(CPP14Parser.LeftParen)
            self.state = 2430
            self.exceptiondeclaration()
            self.state = 2431
            self.match(CPP14Parser.RightParen)
            self.state = 2432
            self.compoundstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExceptiondeclarationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.TypespecifierseqContext,0)


        def declarator(self):
            return self.getTypedRuleContext(CPP14Parser.DeclaratorContext,0)


        def attributespecifierseq(self):
            return self.getTypedRuleContext(CPP14Parser.AttributespecifierseqContext,0)


        def abstractdeclarator(self):
            return self.getTypedRuleContext(CPP14Parser.AbstractdeclaratorContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_exceptiondeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExceptiondeclaration" ):
                listener.enterExceptiondeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExceptiondeclaration" ):
                listener.exitExceptiondeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExceptiondeclaration" ):
                return visitor.visitExceptiondeclaration(self)
            else:
                return visitor.visitChildren(self)




    def exceptiondeclaration(self):

        localctx = CPP14Parser.ExceptiondeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_exceptiondeclaration)
        self._la = 0 # Token type
        try:
            self.state = 2448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,317,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2435
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2434
                    self.attributespecifierseq(0)


                self.state = 2437
                self.typespecifierseq()
                self.state = 2438
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2441
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Alignas or _la==CPP14Parser.LeftBracket:
                    self.state = 2440
                    self.attributespecifierseq(0)


                self.state = 2443
                self.typespecifierseq()
                self.state = 2445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPP14Parser.Decltype or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (CPP14Parser.LeftParen - 80)) | (1 << (CPP14Parser.LeftBracket - 80)) | (1 << (CPP14Parser.Star - 80)) | (1 << (CPP14Parser.And - 80)) | (1 << (CPP14Parser.AndAnd - 80)) | (1 << (CPP14Parser.Doublecolon - 80)) | (1 << (CPP14Parser.Ellipsis - 80)) | (1 << (CPP14Parser.Identifier - 80)))) != 0):
                    self.state = 2444
                    self.abstractdeclarator()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2447
                self.match(CPP14Parser.Ellipsis)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ThrowexpressionContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(CPP14Parser.Throw, 0)

        def assignmentexpression(self):
            return self.getTypedRuleContext(CPP14Parser.AssignmentexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_throwexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowexpression" ):
                listener.enterThrowexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowexpression" ):
                listener.exitThrowexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowexpression" ):
                return visitor.visitThrowexpression(self)
            else:
                return visitor.visitChildren(self)




    def throwexpression(self):

        localctx = CPP14Parser.ThrowexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_throwexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2450
            self.match(CPP14Parser.Throw)
            self.state = 2452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,318,self._ctx)
            if la_ == 1:
                self.state = 2451
                self.assignmentexpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExceptionspecificationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dynamicexceptionspecification(self):
            return self.getTypedRuleContext(CPP14Parser.DynamicexceptionspecificationContext,0)


        def noexceptspecification(self):
            return self.getTypedRuleContext(CPP14Parser.NoexceptspecificationContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_exceptionspecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExceptionspecification" ):
                listener.enterExceptionspecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExceptionspecification" ):
                listener.exitExceptionspecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExceptionspecification" ):
                return visitor.visitExceptionspecification(self)
            else:
                return visitor.visitChildren(self)




    def exceptionspecification(self):

        localctx = CPP14Parser.ExceptionspecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_exceptionspecification)
        try:
            self.state = 2456
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Throw]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2454
                self.dynamicexceptionspecification()
                pass
            elif token in [CPP14Parser.Noexcept]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2455
                self.noexceptspecification()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DynamicexceptionspecificationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(CPP14Parser.Throw, 0)

        def typeidlist(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_dynamicexceptionspecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamicexceptionspecification" ):
                listener.enterDynamicexceptionspecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamicexceptionspecification" ):
                listener.exitDynamicexceptionspecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamicexceptionspecification" ):
                return visitor.visitDynamicexceptionspecification(self)
            else:
                return visitor.visitChildren(self)




    def dynamicexceptionspecification(self):

        localctx = CPP14Parser.DynamicexceptionspecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_dynamicexceptionspecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2458
            self.match(CPP14Parser.Throw)
            self.state = 2459
            self.match(CPP14Parser.LeftParen)
            self.state = 2461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPP14Parser.Auto) | (1 << CPP14Parser.Bool) | (1 << CPP14Parser.Char) | (1 << CPP14Parser.Char16) | (1 << CPP14Parser.Char32) | (1 << CPP14Parser.Class) | (1 << CPP14Parser.Const) | (1 << CPP14Parser.Decltype) | (1 << CPP14Parser.Double) | (1 << CPP14Parser.Enum) | (1 << CPP14Parser.Float) | (1 << CPP14Parser.Int) | (1 << CPP14Parser.Long) | (1 << CPP14Parser.Short) | (1 << CPP14Parser.Signed) | (1 << CPP14Parser.Struct))) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & ((1 << (CPP14Parser.Typename - 71)) | (1 << (CPP14Parser.Union - 71)) | (1 << (CPP14Parser.Unsigned - 71)) | (1 << (CPP14Parser.Void - 71)) | (1 << (CPP14Parser.Volatile - 71)) | (1 << (CPP14Parser.Wchar - 71)) | (1 << (CPP14Parser.Doublecolon - 71)) | (1 << (CPP14Parser.Identifier - 71)))) != 0):
                self.state = 2460
                self.typeidlist(0)


            self.state = 2463
            self.match(CPP14Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeidlistContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeid(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidContext,0)


        def typeidlist(self):
            return self.getTypedRuleContext(CPP14Parser.TypeidlistContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_typeidlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeidlist" ):
                listener.enterTypeidlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeidlist" ):
                listener.exitTypeidlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeidlist" ):
                return visitor.visitTypeidlist(self)
            else:
                return visitor.visitChildren(self)



    def typeidlist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPP14Parser.TypeidlistContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 400
        self.enterRecursionRule(localctx, 400, self.RULE_typeidlist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2466
            self.typeid()
            self.state = 2468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,321,self._ctx)
            if la_ == 1:
                self.state = 2467
                self.match(CPP14Parser.Ellipsis)


            self._ctx.stop = self._input.LT(-1)
            self.state = 2478
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,323,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CPP14Parser.TypeidlistContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_typeidlist)
                    self.state = 2470
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2471
                    self.match(CPP14Parser.Comma)
                    self.state = 2472
                    self.typeid()
                    self.state = 2474
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,322,self._ctx)
                    if la_ == 1:
                        self.state = 2473
                        self.match(CPP14Parser.Ellipsis)

             
                self.state = 2480
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,323,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NoexceptspecificationContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Noexcept(self):
            return self.getToken(CPP14Parser.Noexcept, 0)

        def constantexpression(self):
            return self.getTypedRuleContext(CPP14Parser.ConstantexpressionContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_noexceptspecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoexceptspecification" ):
                listener.enterNoexceptspecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoexceptspecification" ):
                listener.exitNoexceptspecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoexceptspecification" ):
                return visitor.visitNoexceptspecification(self)
            else:
                return visitor.visitChildren(self)




    def noexceptspecification(self):

        localctx = CPP14Parser.NoexceptspecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_noexceptspecification)
        try:
            self.state = 2487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,324,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2481
                self.match(CPP14Parser.Noexcept)
                self.state = 2482
                self.match(CPP14Parser.LeftParen)
                self.state = 2483
                self.constantexpression()
                self.state = 2484
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2486
                self.match(CPP14Parser.Noexcept)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RightShiftContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Greater(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.Greater)
            else:
                return self.getToken(CPP14Parser.Greater, i)

        def getRuleIndex(self):
            return CPP14Parser.RULE_rightShift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRightShift" ):
                listener.enterRightShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRightShift" ):
                listener.exitRightShift(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRightShift" ):
                return visitor.visitRightShift(self)
            else:
                return visitor.visitChildren(self)




    def rightShift(self):

        localctx = CPP14Parser.RightShiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_rightShift)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2489
            self.match(CPP14Parser.Greater)
            self.state = 2490
            self.match(CPP14Parser.Greater)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RightShiftAssignContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Greater(self, i:int=None):
            if i is None:
                return self.getTokens(CPP14Parser.Greater)
            else:
                return self.getToken(CPP14Parser.Greater, i)

        def Assign(self):
            return self.getToken(CPP14Parser.Assign, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_rightShiftAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRightShiftAssign" ):
                listener.enterRightShiftAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRightShiftAssign" ):
                listener.exitRightShiftAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRightShiftAssign" ):
                return visitor.visitRightShiftAssign(self)
            else:
                return visitor.visitChildren(self)




    def rightShiftAssign(self):

        localctx = CPP14Parser.RightShiftAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_rightShiftAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2492
            self.match(CPP14Parser.Greater)
            self.state = 2493
            self.match(CPP14Parser.Greater)
            self.state = 2494
            self.match(CPP14Parser.Assign)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def New(self):
            return self.getToken(CPP14Parser.New, 0)

        def Delete(self):
            return self.getToken(CPP14Parser.Delete, 0)

        def rightShift(self):
            return self.getTypedRuleContext(CPP14Parser.RightShiftContext,0)


        def rightShiftAssign(self):
            return self.getTypedRuleContext(CPP14Parser.RightShiftAssignContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = CPP14Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_operator)
        try:
            self.state = 2544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,325,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2496
                self.match(CPP14Parser.New)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2497
                self.match(CPP14Parser.Delete)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2498
                self.match(CPP14Parser.New)
                self.state = 2499
                self.match(CPP14Parser.LeftBracket)
                self.state = 2500
                self.match(CPP14Parser.RightBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2501
                self.match(CPP14Parser.Delete)
                self.state = 2502
                self.match(CPP14Parser.LeftBracket)
                self.state = 2503
                self.match(CPP14Parser.RightBracket)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2504
                self.match(CPP14Parser.Plus)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2505
                self.match(CPP14Parser.Minus)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2506
                self.match(CPP14Parser.Star)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2507
                self.match(CPP14Parser.Div)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2508
                self.match(CPP14Parser.Mod)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2509
                self.match(CPP14Parser.Caret)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2510
                self.match(CPP14Parser.And)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 2511
                self.match(CPP14Parser.Or)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 2512
                self.match(CPP14Parser.Tilde)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 2513
                self.match(CPP14Parser.Not)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 2514
                self.match(CPP14Parser.Assign)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 2515
                self.match(CPP14Parser.Less)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 2516
                self.match(CPP14Parser.Greater)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 2517
                self.match(CPP14Parser.PlusAssign)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 2518
                self.match(CPP14Parser.MinusAssign)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 2519
                self.match(CPP14Parser.StarAssign)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 2520
                self.match(CPP14Parser.DivAssign)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 2521
                self.match(CPP14Parser.ModAssign)
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 2522
                self.match(CPP14Parser.XorAssign)
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 2523
                self.match(CPP14Parser.AndAssign)
                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 2524
                self.match(CPP14Parser.OrAssign)
                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 2525
                self.match(CPP14Parser.LeftShift)
                pass

            elif la_ == 27:
                self.enterOuterAlt(localctx, 27)
                self.state = 2526
                self.rightShift()
                pass

            elif la_ == 28:
                self.enterOuterAlt(localctx, 28)
                self.state = 2527
                self.rightShiftAssign()
                pass

            elif la_ == 29:
                self.enterOuterAlt(localctx, 29)
                self.state = 2528
                self.match(CPP14Parser.LeftShiftAssign)
                pass

            elif la_ == 30:
                self.enterOuterAlt(localctx, 30)
                self.state = 2529
                self.match(CPP14Parser.Equal)
                pass

            elif la_ == 31:
                self.enterOuterAlt(localctx, 31)
                self.state = 2530
                self.match(CPP14Parser.NotEqual)
                pass

            elif la_ == 32:
                self.enterOuterAlt(localctx, 32)
                self.state = 2531
                self.match(CPP14Parser.LessEqual)
                pass

            elif la_ == 33:
                self.enterOuterAlt(localctx, 33)
                self.state = 2532
                self.match(CPP14Parser.GreaterEqual)
                pass

            elif la_ == 34:
                self.enterOuterAlt(localctx, 34)
                self.state = 2533
                self.match(CPP14Parser.AndAnd)
                pass

            elif la_ == 35:
                self.enterOuterAlt(localctx, 35)
                self.state = 2534
                self.match(CPP14Parser.OrOr)
                pass

            elif la_ == 36:
                self.enterOuterAlt(localctx, 36)
                self.state = 2535
                self.match(CPP14Parser.PlusPlus)
                pass

            elif la_ == 37:
                self.enterOuterAlt(localctx, 37)
                self.state = 2536
                self.match(CPP14Parser.MinusMinus)
                pass

            elif la_ == 38:
                self.enterOuterAlt(localctx, 38)
                self.state = 2537
                self.match(CPP14Parser.Comma)
                pass

            elif la_ == 39:
                self.enterOuterAlt(localctx, 39)
                self.state = 2538
                self.match(CPP14Parser.ArrowStar)
                pass

            elif la_ == 40:
                self.enterOuterAlt(localctx, 40)
                self.state = 2539
                self.match(CPP14Parser.Arrow)
                pass

            elif la_ == 41:
                self.enterOuterAlt(localctx, 41)
                self.state = 2540
                self.match(CPP14Parser.LeftParen)
                self.state = 2541
                self.match(CPP14Parser.RightParen)
                pass

            elif la_ == 42:
                self.enterOuterAlt(localctx, 42)
                self.state = 2542
                self.match(CPP14Parser.LeftBracket)
                self.state = 2543
                self.match(CPP14Parser.RightBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integerliteral(self):
            return self.getToken(CPP14Parser.Integerliteral, 0)

        def Characterliteral(self):
            return self.getToken(CPP14Parser.Characterliteral, 0)

        def Floatingliteral(self):
            return self.getToken(CPP14Parser.Floatingliteral, 0)

        def Stringliteral(self):
            return self.getToken(CPP14Parser.Stringliteral, 0)

        def booleanliteral(self):
            return self.getTypedRuleContext(CPP14Parser.BooleanliteralContext,0)


        def pointerliteral(self):
            return self.getTypedRuleContext(CPP14Parser.PointerliteralContext,0)


        def userdefinedliteral(self):
            return self.getTypedRuleContext(CPP14Parser.UserdefinedliteralContext,0)


        def getRuleIndex(self):
            return CPP14Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CPP14Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_literal)
        try:
            self.state = 2553
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPP14Parser.Integerliteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2546
                self.match(CPP14Parser.Integerliteral)
                pass
            elif token in [CPP14Parser.Characterliteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2547
                self.match(CPP14Parser.Characterliteral)
                pass
            elif token in [CPP14Parser.Floatingliteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2548
                self.match(CPP14Parser.Floatingliteral)
                pass
            elif token in [CPP14Parser.Stringliteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2549
                self.match(CPP14Parser.Stringliteral)
                pass
            elif token in [CPP14Parser.KFalse, CPP14Parser.KTrue]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2550
                self.booleanliteral()
                pass
            elif token in [CPP14Parser.Nullptr]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2551
                self.pointerliteral()
                pass
            elif token in [CPP14Parser.Userdefinedintegerliteral, CPP14Parser.Userdefinedfloatingliteral, CPP14Parser.Userdefinedstringliteral, CPP14Parser.Userdefinedcharacterliteral]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2552
                self.userdefinedliteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanliteralContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KFalse(self):
            return self.getToken(CPP14Parser.KFalse, 0)

        def KTrue(self):
            return self.getToken(CPP14Parser.KTrue, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_booleanliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanliteral" ):
                listener.enterBooleanliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanliteral" ):
                listener.exitBooleanliteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanliteral" ):
                return visitor.visitBooleanliteral(self)
            else:
                return visitor.visitChildren(self)




    def booleanliteral(self):

        localctx = CPP14Parser.BooleanliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_booleanliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2555
            _la = self._input.LA(1)
            if not(_la==CPP14Parser.KFalse or _la==CPP14Parser.KTrue):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PointerliteralContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Nullptr(self):
            return self.getToken(CPP14Parser.Nullptr, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_pointerliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerliteral" ):
                listener.enterPointerliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerliteral" ):
                listener.exitPointerliteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerliteral" ):
                return visitor.visitPointerliteral(self)
            else:
                return visitor.visitChildren(self)




    def pointerliteral(self):

        localctx = CPP14Parser.PointerliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_pointerliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2557
            self.match(CPP14Parser.Nullptr)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UserdefinedliteralContext(PrettyPrintParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Userdefinedintegerliteral(self):
            return self.getToken(CPP14Parser.Userdefinedintegerliteral, 0)

        def Userdefinedfloatingliteral(self):
            return self.getToken(CPP14Parser.Userdefinedfloatingliteral, 0)

        def Userdefinedstringliteral(self):
            return self.getToken(CPP14Parser.Userdefinedstringliteral, 0)

        def Userdefinedcharacterliteral(self):
            return self.getToken(CPP14Parser.Userdefinedcharacterliteral, 0)

        def getRuleIndex(self):
            return CPP14Parser.RULE_userdefinedliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUserdefinedliteral" ):
                listener.enterUserdefinedliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUserdefinedliteral" ):
                listener.exitUserdefinedliteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUserdefinedliteral" ):
                return visitor.visitUserdefinedliteral(self)
            else:
                return visitor.visitChildren(self)




    def userdefinedliteral(self):

        localctx = CPP14Parser.UserdefinedliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_userdefinedliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2559
            _la = self._input.LA(1)
            if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (CPP14Parser.Userdefinedintegerliteral - 137)) | (1 << (CPP14Parser.Userdefinedfloatingliteral - 137)) | (1 << (CPP14Parser.Userdefinedstringliteral - 137)) | (1 << (CPP14Parser.Userdefinedcharacterliteral - 137)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.nestednamespecifier_sempred
        self._predicates[10] = self.capturelist_sempred
        self._predicates[15] = self.postfixexpression_sempred
        self._predicates[24] = self.noptrnewdeclarator_sempred
        self._predicates[29] = self.pmexpression_sempred
        self._predicates[30] = self.multiplicativeexpression_sempred
        self._predicates[31] = self.additiveexpression_sempred
        self._predicates[32] = self.shiftexpression_sempred
        self._predicates[33] = self.relationalexpression_sempred
        self._predicates[34] = self.equalityexpression_sempred
        self._predicates[35] = self.andexpression_sempred
        self._predicates[36] = self.exclusiveorexpression_sempred
        self._predicates[37] = self.inclusiveorexpression_sempred
        self._predicates[38] = self.logicalandexpression_sempred
        self._predicates[39] = self.logicalorexpression_sempred
        self._predicates[45] = self.expression_sempred
        self._predicates[46] = self.co_expression_sempred
        self._predicates[55] = self.statementseq_sempred
        self._predicates[56] = self.co_statementseq_sempred
        self._predicates[66] = self.declarationseq_sempred
        self._predicates[93] = self.enumeratorlist_sempred
        self._predicates[111] = self.attributespecifierseq_sempred
        self._predicates[114] = self.attributelist_sempred
        self._predicates[120] = self.balancedtokenseq_sempred
        self._predicates[122] = self.initdeclaratorlist_sempred
        self._predicates[126] = self.noptrdeclarator_sempred
        self._predicates[137] = self.noptrabstractdeclarator_sempred
        self._predicates[139] = self.noptrabstractpackdeclarator_sempred
        self._predicates[141] = self.parameterdeclarationlist_sempred
        self._predicates[150] = self.initializerlist_sempred
        self._predicates[160] = self.memberdeclaratorlist_sempred
        self._predicates[162] = self.virtspecifierseq_sempred
        self._predicates[166] = self.basespecifierlist_sempred
        self._predicates[181] = self.templateparameterlist_sempred
        self._predicates[187] = self.templateargumentlist_sempred
        self._predicates[200] = self.typeidlist_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def nestednamespecifier_sempred(self, localctx:NestednamespecifierContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def capturelist_sempred(self, localctx:CapturelistContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def postfixexpression_sempred(self, localctx:PostfixexpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 7)
         

    def noptrnewdeclarator_sempred(self, localctx:NoptrnewdeclaratorContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def pmexpression_sempred(self, localctx:PmexpressionContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def multiplicativeexpression_sempred(self, localctx:MultiplicativeexpressionContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         

    def additiveexpression_sempred(self, localctx:AdditiveexpressionContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def shiftexpression_sempred(self, localctx:ShiftexpressionContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 1)
         

    def relationalexpression_sempred(self, localctx:RelationalexpressionContext, predIndex:int):
            if predIndex == 22:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         

    def equalityexpression_sempred(self, localctx:EqualityexpressionContext, predIndex:int):
            if predIndex == 26:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 1)
         

    def andexpression_sempred(self, localctx:AndexpressionContext, predIndex:int):
            if predIndex == 28:
                return self.precpred(self._ctx, 1)
         

    def exclusiveorexpression_sempred(self, localctx:ExclusiveorexpressionContext, predIndex:int):
            if predIndex == 29:
                return self.precpred(self._ctx, 1)
         

    def inclusiveorexpression_sempred(self, localctx:InclusiveorexpressionContext, predIndex:int):
            if predIndex == 30:
                return self.precpred(self._ctx, 1)
         

    def logicalandexpression_sempred(self, localctx:LogicalandexpressionContext, predIndex:int):
            if predIndex == 31:
                return self.precpred(self._ctx, 1)
         

    def logicalorexpression_sempred(self, localctx:LogicalorexpressionContext, predIndex:int):
            if predIndex == 32:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def co_expression_sempred(self, localctx:Co_expressionContext, predIndex:int):
            if predIndex == 34:
                return self.precpred(self._ctx, 1)
         

    def statementseq_sempred(self, localctx:StatementseqContext, predIndex:int):
            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def co_statementseq_sempred(self, localctx:Co_statementseqContext, predIndex:int):
            if predIndex == 36:
                return self.precpred(self._ctx, 1)
         

    def declarationseq_sempred(self, localctx:DeclarationseqContext, predIndex:int):
            if predIndex == 37:
                return self.precpred(self._ctx, 1)
         

    def enumeratorlist_sempred(self, localctx:EnumeratorlistContext, predIndex:int):
            if predIndex == 38:
                return self.precpred(self._ctx, 1)
         

    def attributespecifierseq_sempred(self, localctx:AttributespecifierseqContext, predIndex:int):
            if predIndex == 39:
                return self.precpred(self._ctx, 1)
         

    def attributelist_sempred(self, localctx:AttributelistContext, predIndex:int):
            if predIndex == 40:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 41:
                return self.precpred(self._ctx, 1)
         

    def balancedtokenseq_sempred(self, localctx:BalancedtokenseqContext, predIndex:int):
            if predIndex == 42:
                return self.precpred(self._ctx, 1)
         

    def initdeclaratorlist_sempred(self, localctx:InitdeclaratorlistContext, predIndex:int):
            if predIndex == 43:
                return self.precpred(self._ctx, 1)
         

    def noptrdeclarator_sempred(self, localctx:NoptrdeclaratorContext, predIndex:int):
            if predIndex == 44:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 45:
                return self.precpred(self._ctx, 2)
         

    def noptrabstractdeclarator_sempred(self, localctx:NoptrabstractdeclaratorContext, predIndex:int):
            if predIndex == 46:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 47:
                return self.precpred(self._ctx, 3)
         

    def noptrabstractpackdeclarator_sempred(self, localctx:NoptrabstractpackdeclaratorContext, predIndex:int):
            if predIndex == 48:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 49:
                return self.precpred(self._ctx, 2)
         

    def parameterdeclarationlist_sempred(self, localctx:ParameterdeclarationlistContext, predIndex:int):
            if predIndex == 50:
                return self.precpred(self._ctx, 1)
         

    def initializerlist_sempred(self, localctx:InitializerlistContext, predIndex:int):
            if predIndex == 51:
                return self.precpred(self._ctx, 1)
         

    def memberdeclaratorlist_sempred(self, localctx:MemberdeclaratorlistContext, predIndex:int):
            if predIndex == 52:
                return self.precpred(self._ctx, 1)
         

    def virtspecifierseq_sempred(self, localctx:VirtspecifierseqContext, predIndex:int):
            if predIndex == 53:
                return self.precpred(self._ctx, 1)
         

    def basespecifierlist_sempred(self, localctx:BasespecifierlistContext, predIndex:int):
            if predIndex == 54:
                return self.precpred(self._ctx, 1)
         

    def templateparameterlist_sempred(self, localctx:TemplateparameterlistContext, predIndex:int):
            if predIndex == 55:
                return self.precpred(self._ctx, 1)
         

    def templateargumentlist_sempred(self, localctx:TemplateargumentlistContext, predIndex:int):
            if predIndex == 56:
                return self.precpred(self._ctx, 1)
         

    def typeidlist_sempred(self, localctx:TypeidlistContext, predIndex:int):
            if predIndex == 57:
                return self.precpred(self._ctx, 1)
         




