# ZDI-18-423: SAP MaxDB Data Link Properties Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-423
- **ZDI-CAN:** ZDI-CAN-5478
- **Date:** 2018-05-14
- **CVE:** CVE-2018-2418
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SAP
- **Affected Products:** MaxDB
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-423/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP MaxDB. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of UDL files by the Data Link Properties dialog. When parsing the Servername element, the process does not properly validate the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://blogs.sap.com/2018/05/08/sap-security-patch-day-may-2018/

## Disclosure Timeline

- 2018-01-04 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
