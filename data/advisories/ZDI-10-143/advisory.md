# ZDI-10-143: Novell Sentinel Log Manager Multiple Servlet Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-143
- **ZDI-CAN:** ZDI-CAN-622
- **Date:** 2010-08-09
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Security Manager
- **Credit:** 1c239c43f521145fa8385d64a9c32243
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-143/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Log Manager. Authentication is not required to exploit this vulnerability. The specific flaws exist within the fileDownload and reportPluginUpload Tomcat servlets which do not require authentication to make privileged requests to. Due to the nature of the functionality provided by these servlets, successful exploitation can lead to code execution under the context of the application.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=AhFWOo7BmdQ~

## Disclosure Timeline

- 2009-11-06 - Vulnerability reported to vendor
- 2010-08-09 - Coordinated public release of advisory
