# ZDI-10-292: Hewlett-Packard Power Manager Administration Web Server Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-292
- **ZDI-CAN:** ZDI-CAN-697
- **Date:** 2010-12-16
- **CVE:** CVE-2010-4113
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Power Manager
- **Credit:** Tenable Network Security Andrea Micalizzi aka rgod SilentSignal Anonymous Anonymous Anonymous Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-292/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Power Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of URL parameters when posting to the login form of the web based management web server. Proper bounds checking is not applied when parsing the Login variable which can result in an exploitable stack overflow. Successful exploitation can lead to complete system compromise under the SYSTEM credentials.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02239581

## Disclosure Timeline

- 2010-06-03 - Vulnerability reported to vendor
- 2010-12-16 - Coordinated public release of advisory
