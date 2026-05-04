# ZDI-08-065: Novell eDirectory Core Protocol Opcode 0x0F Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-065
- **ZDI-CAN:** ZDI-CAN-336
- **Date:** 2008-10-08
- **CVE:** CVE-2008-4478
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell eDirectory Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within dhost.exe, the service responsible for directory replication which is bound by default to TCP port 524. Improper parsing within opcode 0x0F via the Netware Core Protocol can result in an arithmetic calculation based on supplied user-input resulting in an integer overflow that will be used to copy into a heap buffer. This fault can be leveraged to result in arbitrary code execution.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=7001184&sliceId=1&docTypeID=DT_TID_1_1&dialogID=78066829&stateId=0%200%2078062953

## Disclosure Timeline

- 2008-05-19 - Vulnerability reported to vendor
- 2008-10-08 - Coordinated public release of advisory
