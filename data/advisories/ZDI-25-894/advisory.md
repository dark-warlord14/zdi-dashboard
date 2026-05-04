# ZDI-25-894: Digilent WaveForms DWF3WORK File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-894
- **ZDI-CAN:** ZDI-CAN-26583
- **Date:** 2025-09-16
- **CVE:** CVE-2025-10203
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Digilent
- **Affected Products:** WaveForms
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-894/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Digilent WaveForms. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of DWF3WORK files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Digilent has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/relative-path-traversal-vulnerability-in-digilent-waveforms.html

## Disclosure Timeline

- 2025-07-24 - Vulnerability reported to vendor
- 2025-09-16 - Coordinated public release of advisory
- 2025-09-16 - Advisory Updated
