# ZDI-21-772: (Pwn2Own) Microsoft Teams ElectronJS Frame Redirect Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-772
- **ZDI-CAN:** ZDI-CAN-13612
- **Date:** 2021-07-05
- **CVE:** N/A
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** oskarsv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-772/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams Desktop. An attacker must first obtain the ability to execute arbitrary JavaScript within an iframe within the application window in order to exploit this vulnerability. The specific flaw exists within the protection of the top ElectronJS frame. By performing actions in JavaScript, an attacker can navigate the top frame to a malicious page, thereby gaining access to internal application objects. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

fixed in version 1.4.00.11161

## Disclosure Timeline

- 2021-04-19 - Vulnerability reported to vendor
- 2021-07-05 - Coordinated public release of advisory
