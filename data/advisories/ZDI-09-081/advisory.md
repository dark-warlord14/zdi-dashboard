# ZDI-09-081: Hewlett-Packard Power Manager Administration Web Server Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-081
- **ZDI-CAN:** ZDI-CAN-492
- **Date:** 2009-11-05
- **CVE:** CVE-2009-2685
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Power Manager
- **Credit:** Janek Vind
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-081/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Power Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of URL parameters when posting to the login form of the web based management web server. Proper bounds checking is not applied when parsing the Login variable which can result in an exploitable stack overflow. Successful exploitation can lead to complete system compromise under the SYSTEM credentials.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01905743

## Disclosure Timeline

- 2009-06-25 - Vulnerability reported to vendor
- 2009-11-05 - Coordinated public release of advisory
