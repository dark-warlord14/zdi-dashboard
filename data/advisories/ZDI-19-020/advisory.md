# ZDI-19-020: Schneider Electric IIoT Monitor downloadCSV Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-020
- **ZDI-CAN:** ZDI-CAN-7118
- **Date:** 2019-01-14
- **CVE:** CVE-2018-7835
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IIot Monitor
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-020/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Schneider Electric IIoT Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists within downloadCSV.jsp servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose sensitive information in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-008-02

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-14 - Coordinated public release of advisory
