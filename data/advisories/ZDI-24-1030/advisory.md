# ZDI-24-1030: NI VeriStand VSMODEL File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1030
- **ZDI-CAN:** ZDI-CAN-22009
- **Date:** 2024-07-30
- **CVE:** CVE-2024-6791
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** VeriStand
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI VeriStand. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VSMODEL files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/directory-path-traversal-vulnerability-in-ni-veristand-with-vsmodel-files.html

## Disclosure Timeline

- 2024-03-15 - Vulnerability reported to vendor
- 2024-07-30 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
