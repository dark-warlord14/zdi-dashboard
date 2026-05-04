# ZDI-25-707: AVG TuneUp for PC TuneUp Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-707
- **ZDI-CAN:** ZDI-CAN-23383
- **Date:** 2025-07-29
- **CVE:** CVE-2024-13960
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** AVG
- **Affected Products:** TuneUp for PC
- **Credit:** Naor Hodorov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-707/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of AVG TuneUp for PC. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TuneUp Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed with Tuneup v24.1 31.7.2024

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
