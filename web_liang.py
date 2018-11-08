
file_dir = "/Users/lli51/Documents/Jiafu_Web/tmp_png/"
web_dir ='/Users/lli51/Documents/Jiafu_Web/'

# variablelist = ['GPP', 'HR']
# variablelongnamelist = ['GPP', 'HR']

with open(file_dir+'3D_vars_name_for_ann.txt', 'r') as myfile:
    variablelist=myfile.read().split('\n')
with open(file_dir+'3D_vars_longname_for_ann.txt', 'r') as myfile:
    variablelongnamelist=myfile.read().split('\n')

featherlist= ['Gsurf_mean','Gsurf_stan','Gsurf_slope','MsurfMean_MaxTiming','MsurfMean_MinTiming',
              'MZsurf_mean','MZsurf_slope','Zsurf_mean', 'Zsurf_anom', 'Zline_mean',
              'Zline_slope', 'lines_sum', 'lines_annualC_sum','lines_annualC_slope']
feathername= ['GLOBAL MEANS','GLOBAL STANDARD DEVIATIONS','GLOBAL TRENDS','GLOBAL TIMING OF MAXIMUM','GLOBAL TIMING OF MINIMUM',
              'ZONAL-MONTH MEANS','ZONAL-MONTH TRENDS','ZONAL-YEAR EVOLUTION','ZONAL-YEAR ANOMALY EVOLUTION','ZONAL MEAN SUMMARIES',
              'ZONAL MEAN TRENDS', 'REGIONAL TIME SERIES','REGIONAL MEAN ANNUAL CYCLES','REGIONAL ANNUAL CYCLE TRENDS']

front = """

<html>
  <head>
    <title>Results</title>
    <link rel="stylesheet" href="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css"></link>
    <script src="https://code.jquery.com/jquery-1.11.2.min.js"></script>
    <script>
      $(document).bind('mobileinit',function(){
      $.mobile.changePage.defaults.changeHash = false;
      $.mobile.hashListeningEnabled = false;
      $.mobile.pushStateEnabled = false;
      });
    </script>
    <script src="https://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">  
      $(document).ready(function(){
      function getChildren($row) {
      var children = [];
      while($row.next().hasClass('child')) {
      children.push($row.next());
      $row = $row.next();
      }            
      return children;
      }
      $('.parent').on('click', function() {
      $(this).find(".arrow").toggleClass("up");
      var children = getChildren($(this));
      $.each(children, function() {
      $(this).toggle();
      })
      });
      $('.child').toggle();
      });
    </script>
    <style>
      div.arrow {
        background:transparent url(arrows.png) no-repeat scroll 0px -16px;
        width:16px;
        height:16px; 
        display:block;
      }
      div.up {
        background-position:0px 0px;
      }
      .child {
      }
      .parent {
        cursor:pointer;
      }
      th {
        border-bottom: 1px solid #d6d6d6;
      }
      img.displayed {
        display: block;
        margin-left: auto;
        margin-right: auto
      }
    </style>
  </head>

  <body>
    <div data-role="page" id="pageOverview">
      <div data-role="header" data-position="fixed" data-tap-toggle="false">
	<h1> The length of the diagnostics is between 1850 and 2010. </h1>
	<h2> The legend of individual models is at <a href="./tmp_png/Legend_models.png" rel="external" target="_blank">HERE</a>  </h2>
	<div data-role="navbar">
	  <ul>
	    <li><a href="#pageTable">Results</a></li>
	  </ul>
	</div>
      </div>
        <div data-role="main" class="ui-content">
<!--        <div data-role="collapsible" data-collapsed="false"> <h1>Output Results1</h1>-->
	<table data-role="table" data-mode="columntoggle" class="ui-responsive ui-shadow" id="meanTable">
<thead>
	    <tr>
              <th data-priority="1">Short Name </th>
              <th data-priority="1">Long Name </th>
              <th data-priority="1">DJF</th>
              <th data-priority="1">MAM</th>
              <th data-priority="1">JJA</th>
              <th data-priority="1">SON</th>
              <th data-priority="1">AM</th>
              <th data-priority="1">GS</th>
              <th data-priority="1">SO</th>
              <th data-priority="1">ANN</th>
              <th style="width:20px"></th>
	    </tr>
	  </thead>
          <tbody>
          """


tail  = """ </tbody>
</table>
<!--        </div>-->
</div>
</div>

</body>
</html>


"""

def strToFile(text, web_dir, web_name):
    """Write a file with the given name and the given text."""
    output = open(web_dir + web_name, "w")
    output.write(text)
    output.close()

def browseLocal(webpageText, web_dir, web_name):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, web_dir, web_name)
    webbrowser.open(os.path.abspath(web_dir + web_name))  # elaborated for Mac




body = """ """

import os
ad = []
for d in os.listdir(file_dir):
    ad.append(d)
ad.sort()

others = []
for j, var in enumerate(variablelist):
    # feathers = [[]]*len(featherlist)
    feather0,feather1,feather2,feather3,feather4,feather5,feather6,feather7,feather8,feather9,feather10,feather11,feather12,feather13 = [], [], [], [], [], [], [], [], [], [], [], [], [], []
    variable_parent = """
                          <tr class="parent" bgcolor="#ECFFE6">
                          <td> %s </td> <td> %s </td>
                          <td>   </td><td>   </td><td>   </td><td>   </td> <td>   </td><td>   </td><td>   </td><td>   </td>
                          <td><div class="arrow"></div></td></tr>""" % (var,variablelongnamelist[j])
    body += variable_parent

    var_files=[]
    for d in ad:
        if d.startswith(var):
            var_files.append(d)

    for file in var_files:
        tmp = file.split('.')
        # for ind_ in range(len(featherlist)):
        #     if featherlist[ind_] in tmp:
        #         feathers[ind_].append(file)
        #         print(feathers[ind_])
        # else:
        #     others.append(file)
        if featherlist[0] in tmp:
            feather0.append(file)
        elif featherlist[1] in tmp:
            feather1.append(file)
        elif featherlist[2] in tmp:
            feather2.append(file)
        elif featherlist[3] in tmp:
            feather3.append(file)
        elif featherlist[4] in tmp:
            feather4.append(file)
        elif featherlist[5] in tmp:
            feather5.append(file)
        elif featherlist[6] in tmp:
            feather6.append(file)
        elif featherlist[7] in tmp:
            feather7.append(file)
        elif featherlist[8] in tmp:
            feather8.append(file)
        elif featherlist[9] in tmp:
            feather9.append(file)
        elif featherlist[10] in tmp:
            feather10.append(file)
        elif featherlist[11] in tmp:
            feather11.append(file)
        elif featherlist[12] in tmp:
            feather12.append(file)
        elif featherlist[13] in tmp:
            feather13.append(file)
        else:
            others.append(file)

    feathers = [feather0,feather1,feather2,feather3,feather4,feather5,feather6,feather7,feather8,feather9,feather10,feather11,feather12,feather13]
    for i, feather in enumerate(feathers):
        if len(feather)==1:
            variable_child = """ <tr class="child" bgcolor="#e0f2da">
                                      <td>&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;</td>
                                      <td> </td> <td>%s</td>  <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td> <td><div class="arrow"></div></td></tr>
                        """ % (f, feathername[i], '-- ', '-- ', '-- ', '-- ', '-- ', '-- ', '-- ', '-- ')
        else:
            link = feathername[i]
            linkDJF, linkMAM, linkJJA, linkSON = '-- ', '-- ', '-- ', '-- '
            linkam, linkann, linkgs, linkso = '--', '-- ', '-- ', '-- '
            for f in feather:
                if 'mam' in f:
                    # print('mam')
                    linkMAM = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'MAM')
                elif 'son' in f:
                    # print('son')
                    linkSON = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'SON')
                elif 'ann' in f:
                    # print('ann')
                    linkann = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'ANN')
                elif 'gs' in f:
                    # print('gs')
                    linkgs = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'GS')
                elif 'djf' in f:
                    # print('djf')
                    linkDJF = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'DJF')
                elif 'jja' in f:
                    # print('jja')
                    linkJJA = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'JJA')
                elif 'am' in f:
                    # print('am')
                    linkam = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'AM')
                elif 'so' in f:
                    # print('so')
                    linkso = '&nbsp;&nbsp;&nbsp;<a href="./tmp_png/%s" rel="external" target="_blank">%s</a>&nbsp;' %(f, 'SO')
                else:
                    others.append(f)

            variable_child = """ <tr class="child" bgcolor="#e0f2da">
                              <td> %s </td><td>   </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td>
                                                        <td><div class="arrow"></div></td></tr>
                """ % (link, linkDJF, linkMAM, linkJJA, linkSON, linkam, linkgs, linkso, linkann)
        body += variable_child

contents = front + body + tail
browseLocal(contents, web_dir, 'Website_lli.html')

# print('These files need to be added', others)
# print('\n')
print('The website is generated to ' + web_dir + 'Website_lli.html')
