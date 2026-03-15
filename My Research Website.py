from flask import Flask, render_template_string
import os

app = Flask(__name__)

profile = {
    "name": "张三",
    "title": "北京大学化学与分子工程学院 教授",
    "email": "zhangsan@pku.edu.cn",
    "office": "北京大学化学楼 XXX",
    "intro": "张三，北京大学化学与分子工程学院教授，博士生导师。",
    "research_interests": [
        "金属有机框架材料（MOFs）",
        "多孔材料的气体吸附与分离",
        "功能配位化学",
        "环境与能源材料"
    ],
    "awards": [
        "国家自然科学奖二等奖（示例）",
        "教育部自然科学奖一等奖（示例）"
    ],
    "publications": [
        "Zhang S.*, Li X. Title of Paper. Journal Name, 2025, 12, 1234–1245."
    ]
}

html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{{ profile.name }} - 个人主页</title>
    <style>
        body {
            margin: 0;
            font-family: "Times New Roman", "Microsoft YaHei", serif;
            background: #f5f7fa;
            color: #222;
        }
        .container {
            width: 80%;
            max-width: 1000px;
            margin: 40px auto;
            background: white;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-radius: 12px;
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #8b0000, #b22222);
            color: white;
            padding: 40px;
        }
        .header h1 { margin: 0; font-size: 40px; }
        .header h2 { margin-top: 10px; font-weight: normal; font-size: 22px; }
        .content { padding: 35px 40px; }
        .section { margin-bottom: 35px; }
        .section h3 {
            border-left: 5px solid #8b0000;
            padding-left: 12px;
            font-size: 24px;
            margin-bottom: 15px;
            color: #8b0000;
        }
        ul { padding-left: 22px; }
        li { margin-bottom: 10px; line-height: 1.7; font-size: 17px; }
        .footer {
            text-align: center;
            padding: 20px;
            background: #f0f0f0;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{{ profile.name }}</h1>
            <h2>{{ profile.title }}</h2>
        </div>

        <div class="content">
            <div class="section">
                <h3>个人基本信息</h3>
                <p><strong>邮箱：</strong>{{ profile.email }}</p>
                <p><strong>办公室：</strong>{{ profile.office }}</p>
                <p><strong>简介：</strong>{{ profile.intro }}</p>
            </div>

            <div class="section">
                <h3>研究兴趣</h3>
                <ul>
                    {% for item in profile.research_interests %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>

            <div class="section">
                <h3>获奖情况</h3>
                <ul>
                    {% for item in profile.awards %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>

            <div class="section">
                <h3>论文发表</h3>
                <ul>
                    {% for item in profile.publications %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>

        <div class="footer">
            © 2026 {{ profile.name }}
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, profile=profile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
