# ZDI-25-078: NI Vision Builder AI JPG File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-078
- **ZDI-CAN:** ZDI-CAN-22884
- **Date:** 2025-02-03
- **CVE:** CVE-2024-12740
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** Vision Builder AI
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-078/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI Vision Builder AI. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPG files referenced from a VBAI file. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/dependency-on-vulnerable-third-party-component-exposes-vulnerabi.html

## Disclosure Timeline

- 2024-01-17 - Vulnerability reported to vendor
- 2025-02-03 - Coordinated public release of advisory
- 2025-02-03 - Advisory Updated
