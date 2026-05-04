# ZDI-14-302: SAP Crystal Reports Connection String Processing Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-302
- **ZDI-CAN:** ZDI-CAN-2143
- **Date:** 2014-09-03
- **CVE:** CVE-2014-5506
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** Crystal Reports
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-302/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP Crystal Reports. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RPT files. The issue lies in processing a connection string record. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: http://service.sap.com/sap/support/notes/1999142

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-09-03 - Coordinated public release of advisory
