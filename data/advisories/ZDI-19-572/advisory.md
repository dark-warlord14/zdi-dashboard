# ZDI-19-572: Microsoft Word Table Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-572
- **ZDI-CAN:** ZDI-CAN-8531
- **Date:** 2019-06-14
- **CVE:** CVE-2019-1035
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** L4Nce
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-572/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of tables in Microsoft Word documents. Crafted data in a document can trigger a memory access past the end of an array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1035

## Disclosure Timeline

- 2019-04-17 - Vulnerability reported to vendor
- 2019-06-14 - Coordinated public release of advisory
