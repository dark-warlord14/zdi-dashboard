# ZDI-25-967: Delta Electronics CNCSoft-G2 DPAX File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-967
- **ZDI-CAN:** ZDI-CAN-25407
- **Date:** 2025-10-27
- **CVE:** CVE-2025-58319
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** CNCSoft-G2
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-967/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics CNCSoft-G2. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPAX files in the DOPSoft component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://filecenter.deltaww.com/news/download/doc/Delta-PCSA-2025-00017_CNCSoft-G2_File%20Parsing%20Stack-based%20Buffer%20Overflow%20Vulnerability.pdf

## Disclosure Timeline

- 2025-06-30 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
