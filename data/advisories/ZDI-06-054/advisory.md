# ZDI-06-054: Novell NetMail IMAP APPEND Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-054
- **ZDI-CAN:** ZDI-CAN-086
- **Date:** 2006-12-22
- **CVE:** CVE-2006-6425
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** NetMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-054/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Novell NetMail. Successful exploitation requires the attacker to successfully authenticate to the affected service. The specific flaw exists in the NetMail IMAP server's handling of the APPEND command. A lack of bounds checking on a specific parameter to this command can lead to a stack-based buffer overflow. This vulnerability can be exploited to execute arbitrary code.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&externalId=3096026&sliceId=SAL_Public

## Disclosure Timeline

- 2006-08-14 - Vulnerability reported to vendor
- 2006-12-22 - Coordinated public release of advisory
