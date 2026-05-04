# ZDI-21-1329: Commvault CommCell DataProvider JavaScript Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1329
- **ZDI-CAN:** ZDI-CAN-13755
- **Date:** 2021-11-22
- **CVE:** CVE-2021-34994
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Commvault
- **Affected Products:** CommCell
- **Credit:** Brandon Perry, Justin Kennedy and Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1329/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Commvault CommCell. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the DataProvider class. The issue results from the lack of proper validation of a user-supplied string before executing it as JavaScript code. An attacker can leverage this vulnerability to escape the JavaScript sandbox and execute Java code in the context of NETWORK SERVICE.

## Additional Details

Fixed in Version 11.25

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-22 - Coordinated public release of advisory
