# ZDI-21-1331: Commvault CommCell Demo_ExecuteProcessOnGroup Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1331
- **ZDI-CAN:** ZDI-CAN-13889
- **Date:** 2021-11-22
- **CVE:** CVE-2021-34996
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Commvault
- **Affected Products:** CommCell
- **Credit:** Brandon Perry, Justin Kennedy and Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1331/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Commvault CommCell. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Demo_ExecuteProcessOnGroup workflow. By creating a workflow, an attacker can specify an arbitrary command to be executed. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Fixed in Version 11.25

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-22 - Coordinated public release of advisory
