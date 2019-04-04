#coding=utf-8

#通过minidom解析xml文件
import xml.dom.minidom as xmldom
import os
import sys

class XMLResolve():

    #获取 某类标签的所有属性值
    @staticmethod
    def getElementAttribute(xmlfilepath,elementName,elementAttribute):
        # 得到文档对象
        domobj = xmldom.parse(xmlfilepath)
        # 得到元素对象
        elementobj = domobj.documentElement
        # 获得子标签
        subElementObj = elementobj.getElementsByTagName(elementName)
        # 获得标签属性值
        for i in range(len(subElementObj)):
            print (subElementObj[i].getAttribute(elementAttribute))

    #获取某标签下某属性值  该标签需提供 属性及属性值来查找 而且该属性及值是唯一
    @staticmethod
    def getElementAttributeValueByKV(xmlfilepath,elementName,elementAttribute,elementAttributeValue):
        # 得到文档对象
        domobj = xmldom.parse(xmlfilepath)
        # 得到元素对象
        elementobj = domobj.documentElement
        # 获得子标签
        subElementObj = elementobj.getElementsByTagName(elementName)
        # 获得标签属性值
        for element in subElementObj:
            if element.getAttribute(elementAttribute) == elementAttributeValue:
                for key in element.attributes.keys():
                    attr = element.attributes[key]
                    value = attr.value
                    print key+"="+value

    # 获取某标签下某属性值  该标签需提供 属性及属性值来查找 而且该属性及值是唯一
    @staticmethod
    def getElementAttributeValueByKVA(xmlfilepath, elementName, elementAttribute, elementAttributeValue,requireAttributeValueByAttribute):
        # 得到文档对象
        domobj = xmldom.parse(xmlfilepath)
        # 得到元素对象
        elementobj = domobj.documentElement
        # 获得子标签
        subElementObj = elementobj.getElementsByTagName(elementName)
        # 获得标签属性值
        for element in subElementObj:
            if element.getAttribute(elementAttribute) == elementAttributeValue:
                for key in element.attributes.keys():
                    attr = element.attributes[key]
                    value = attr.value
                    if key == requireAttributeValueByAttribute:
                        print attr.value

    #根据标签名字获取标签
    def getElementByName(self,xmlfilepath,tagElement,elementName):
        # 得到文档对象
        domobj = xmldom.parse(xmlfilepath)
        # 得到元素对象
        elementobj = domobj.documentElement
        # 获得子标签
        subElementObj = elementobj.getElementsByTagName(tagElement)
        #print (len(subElementObj))
        # 获得标签属性值
        for i in range(len(subElementObj)):
            print (subElementObj[i].getAttribute("name"))
            print (subElementObj[i].getAttribute("fetch"))
            print (subElementObj[i].getAttribute("review"))

   # def predict(self, x):
    #    check_ans = eval("Test." + Test.state2function[state])(x)  # 调用Test类中的方法

if __name__ == '__main__':
    xmlFile = sys.argv[1] #拿到xml 文件
    if not os.path.exists(xmlFile):
        print (xmlFile,"文件不存在")
        exit(0)
    xmlResolve = XMLResolve()#xmlFile
    functionName=sys.argv[2] #要执行python 代码的那个方法名
    argcount = 0
    if not hasattr(xmlResolve,functionName):
        print ("没有你所请求的%s方法属性"%(functionName))
        exit(0)
    else:
        fun = getattr(xmlResolve,functionName)
        argcount = fun.__code__.co_argcount

    args = [xmlFile] + sys.argv[3:len(sys.argv)]
    #print args
    if len(args) != argcount:
        print "参数个人不匹配,已经给到%d参数,需要%d参数"%(len(args),argcount)
        exit(0)
    kwargs = {}
    eval("XMLResolve."+functionName)(*args, **kwargs) # 使用这个动态调用方法 、必须在方法头部 加上 @staticmethod

