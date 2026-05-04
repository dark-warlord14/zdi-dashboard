# ZDI-20-651: (Pwn2Own) Adobe Acrobat Reader DC Field Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-651
- **ZDI-CAN:** ZDI-CAN-10784
- **Date:** 2020-05-12
- **CVE:** CVE-2020-9606
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-651/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Adobe Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Field objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-24.html

## Disclosure Timeline

- 2020-03-25 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
- 2020-08-18 - Advisory Updated
