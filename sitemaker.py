import os
from pieces import top_HTML, bottom_HTML

page = top_HTML

for root, dirs, files in os.walk('img'):
    for pic in sorted(files):
        # use only the dated pictures
        if pic.startswith('2019'):
            section = f"""        <section class="row mt-5">
                    <div class="col-md-8">
                        <section>
                            <h1>{pic[:-4]}</h1>
                            <p>Today he ate: ???</p>
                            <img src="{root}/{pic}" alt="empty food plate today" class="img-fluid">
                        </section>
                    </div>
                    <div class="col-md-4">
                        <h2 class="display-4">Thoughts...</h2>
                        <blockquote class="blockquote font-italic">
                            <!-- TODO: change for API response -->
                            A lonely crumb is all that's left...
                            <p class="blockquote-footer">Daniel Daniel Wegmann</p>
                        </blockquote>
                    </div>
                </section>"""
        else:
            section = f"""        <section class="row mt-5">
                    <div class="col-md">
                        <section>
                            <img src="{root}/{pic}" alt="empty food plate today" class="img-fluid">
                        </section>
                    </div>
                </section>"""
        page += section

page += bottom_HTML

with open('index.html', 'w') as fout:
    fout.write(page)
