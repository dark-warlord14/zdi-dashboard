# ZDI-25-411: Delta Electronics CNCSoft-G2 DPAX File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-411
- **ZDI-CAN:** ZDI-CAN-26167
- **Date:** 2025-06-19
- **CVE:** CVE-2025-47728
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** CNCSoft-G2
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-411/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics CNCSoft-G2. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPAX files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://filecenter.deltaww.com/news/download/doc/Delta-PCSA-2025-00007_CNCSoft-G2%20-%20File%20Parsing%20Memory%20Corruption.pdf

## Disclosure Timeline

- 2025-02-20 - Vulnerability reported to vendor
- 2025-06-19 - Coordinated public release of advisory
- 2025-06-19 - Advisory Updated
