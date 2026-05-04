# ZDI-26-235: Digilent DASYLab DSA File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-235
- **ZDI-CAN:** ZDI-CAN-28446
- **Date:** 2026-03-30
- **CVE:** CVE-2026-0957
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Digilent
- **Affected Products:** DASYLab
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-235/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Digilent DASYLab. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DSA files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Digilent has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/2026/out-of-bounds-write-vulnerabilities-in-digilent-dasylab.html?srsltid=AfmBOooK3xaKwRhEH_bORQ6hk2CZpAdRYBNIzy6RmFQMec0H4DbTp7HO

## Disclosure Timeline

- 2025-12-09 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
