# ZDI-20-715: Docker Desktop Execution with Unnecessary Privileges Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-715
- **ZDI-CAN:** ZDI-CAN-10074
- **Date:** 2020-06-15
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** 0-duke
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-715/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Troubleshoot functionality. When performing Troubleshoot, Docker executes user-supplied script with unnecessary privilege. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

This was fixed in Docker Desktop Stable: 2.3.0.2 Enterprise: 2.3.0.0-ent Edge: 2.2.3.0

## Disclosure Timeline

- 2020-01-21 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
