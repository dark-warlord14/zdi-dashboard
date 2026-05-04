# ZDI-10-026: Hewlett-Packard OVPI helpmanager Servlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-026
- **ZDI-CAN:** ZDI-CAN-474
- **Date:** 2010-03-09
- **CVE:** CVE-2010-0447
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** OpenView Performance Insight
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary commands on vulnerable installations of Hewlett-Packard Performance Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the helpmanager servlet running on the Performance Insight web server. Insufficient input validation and authentication allows for arbitrary JSP pages to be uploaded which can be leveraged to execute arbitrary OS commands. Exploitation of this vulnerability allows an attacker to gain control of the affected system under SYSTEM credentials.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02033170

## Disclosure Timeline

- 2009-04-15 - Vulnerability reported to vendor
- 2010-03-09 - Coordinated public release of advisory
