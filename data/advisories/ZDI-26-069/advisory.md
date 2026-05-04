# ZDI-26-069: (0Day) Xmind Attachment Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-069
- **ZDI-CAN:** ZDI-CAN-26034
- **Date:** 2026-02-06
- **CVE:** CVE-2026-0777
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xmind
- **Affected Products:** Xmind
- **Credit:** AspiringYoungMan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-069/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Xmind. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of attachments. When opening an attachment, the user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to execute code in the context of current user.

## Additional Details

09/22/25 – ZDI submitted the report to the vendor 09/24/25 – ZDI asked to confirm the receipt of the report 11/11/25 – ZDI asked for updates 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: On 02/10/2026, the vendor confirmed that the issue was mitigated in Xmind version 26.02 https://xmind.com/download

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2026-02-06 - Coordinated public release of advisory
- 2026-02-13 - Advisory Updated
