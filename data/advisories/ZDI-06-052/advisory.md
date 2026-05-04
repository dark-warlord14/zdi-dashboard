# ZDI-06-052: Novell NetMail NMAP STOR Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-052
- **ZDI-CAN:** ZDI-CAN-082
- **Date:** 2006-12-22
- **CVE:** CVE-2006-6424
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** NetMail
- **Credit:** Dennis Rand - CIRT.DK
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Novell NetMail. Successful exploitation requires the attacker to successfully authenticate to the affected service. The specific flaw exists in NetMail's implementation of the Network Messaging Application Protocol (NMAP). The NMAP server lacks bounds checking on parameters supplied to the STOR command, which can lead to an exploitable buffer overflow. The vulnerable daemon, nmapd.exe, binds to TCP port 689.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&externalId=3096026&sliceId=SAL_Public

## Disclosure Timeline

- 2006-09-08 - Vulnerability reported to vendor
- 2006-12-22 - Coordinated public release of advisory
