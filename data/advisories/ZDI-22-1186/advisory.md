# ZDI-22-1186: (Pwn2Own) ConnMan wispr_portal_web_result wp_object Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1186
- **ZDI-CAN:** ZDI-CAN-17447
- **Date:** 2022-09-08
- **CVE:** CVE-2022-32293
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** ConnMan
- **Affected Products:** ConnMan
- **Credit:** David BERARD and Vincent DEHORS from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1186/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of ConnMan. Authentication is not required to exploit this vulnerability. The specific flaw exists within the wispr_portal_web_result method. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the ConnMan process. This vulnerability was demonstrated on a Tesla Model 3 during Pwn2Own 2022 Vancouver competition.

## Additional Details

https://git.kernel.org/pub/scm/network/connman/connman.git/commit/?id=72343929836de80727a27d6744c869dff045757c https://git.kernel.org/pub/scm/network/connman/connman.git/commit/?id=416bfaff988882c553c672e5bfc2d4f648d29e8a

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-09-08 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
