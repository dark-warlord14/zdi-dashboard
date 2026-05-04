# ZDI-17-286: LAquis SCADA Software Web Server Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-286
- **ZDI-CAN:** ZDI-CAN-4523
- **Date:** 2017-04-12
- **CVE:** CVE-2017-6020
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Karn Ganeshen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-286/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of LAquis SCADA Software. Authentication is not required to exploit this vulnerability. The specific flaw exists within global processing of requests inside the web server. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of the web server process.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-082-01

## Disclosure Timeline

- 2017-02-16 - Vulnerability reported to vendor
- 2017-04-12 - Coordinated public release of advisory
