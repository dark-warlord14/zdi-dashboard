# ZDI-26-290: NI LabVIEW LVLIB File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-290
- **ZDI-CAN:** ZDI-CAN-28463
- **Date:** 2026-04-15
- **CVE:** CVE-2026-32860
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** LabVIEW
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI LabVIEW. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LVLIB files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/2026/lv-project-library-file-parsing-memory-corruption-vulnerability-in-ni-labview.html

## Disclosure Timeline

- 2026-02-11 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
