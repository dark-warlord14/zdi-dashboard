# ZDI-19-709: Microsoft Windows xxxMNDragOver Null Pointer Dereference Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-709
- **ZDI-CAN:** ZDI-CAN-8422
- **Date:** 2019-08-13
- **CVE:** CVE-2019-1169
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** kkokkokye@THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-709/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of popup menus. By destroying a menu during a callback, an attacker can trigger a dereference of a null pointer. An attacker can leverage this vulnerability to disclose information in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1169

## Disclosure Timeline

- 2019-05-02 - Vulnerability reported to vendor
- 2019-08-13 - Coordinated public release of advisory
