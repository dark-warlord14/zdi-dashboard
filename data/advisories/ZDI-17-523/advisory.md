# ZDI-17-523: Dell Storage Manager EmWebsiteServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-523
- **ZDI-CAN:** ZDI-CAN-4459
- **Date:** 2017-08-02
- **CVE:** CVE-2017-10949
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Dell EMC
- **Affected Products:** Storage Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-523/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Dell Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the doGet method of the EmWebsiteServlet class, which listens on TCP port 3033 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

Dell EMC has issued an update to correct this vulnerability. More details can be found at: http://topics-cdn.dell.com/pdf/dell-compellent-sc8000_release%20notes24_en-us.pdf

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-08-02 - Coordinated public release of advisory
