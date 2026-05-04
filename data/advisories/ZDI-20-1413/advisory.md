# ZDI-20-1413: Microsoft Chakra LinearScan Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1413
- **ZDI-CAN:** ZDI-CAN-11906
- **Date:** 2020-12-09
- **CVE:** CVE-2020-17131
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Bruno Keith (@bkth_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1413/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JIT compiler. By performing actions in JavaScript, an attacker can trigger a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17131

## Disclosure Timeline

- 2020-09-25 - Vulnerability reported to vendor
- 2020-12-09 - Coordinated public release of advisory
