# ZDI-25-1070: TradingView Desktop Electron Uncontrolled Search Path Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1070
- **ZDI-CAN:** ZDI-CAN-27395
- **Date:** 2025-12-10
- **CVE:** CVE-2025-14498
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TradingView
- **Affected Products:** Desktop
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1070/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of TradingView Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of the Electron framework. The product loads a script file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Fixed in version 2.13.0 ( https://www.tradingview.com/support/solutions/43000673888-tradingview-desktop-releases-and-release-notes/ )

## Disclosure Timeline

- 2025-07-18 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
