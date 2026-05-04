# ZDI-25-710: SolarWinds Platform SolarWindsAgent64 Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-710
- **ZDI-CAN:** ZDI-CAN-24672
- **Date:** 2025-07-29
- **CVE:** CVE-2024-45710
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Platform
- **Credit:** Will Dormann
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-710/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds Platform. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SolarWindsAgent64 service. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2024-45710

## Disclosure Timeline

- 2024-07-25 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
