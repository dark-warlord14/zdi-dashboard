# ZDI-25-1014: Fortinet FortiWeb policy_scripting_post_handler Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1014
- **ZDI-CAN:** ZDI-CAN-27383
- **Date:** 2025-11-19
- **CVE:** CVE-2025-58034
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the policy_scripting_post_handler method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-25-513

## Disclosure Timeline

- 2025-06-10 - Vulnerability reported to vendor
- 2025-11-19 - Coordinated public release of advisory
- 2025-11-19 - Advisory Updated
