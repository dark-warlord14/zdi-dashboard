# ZDI-23-458: SolarWinds Network Performance Monitor TFTP Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-458
- **ZDI-CAN:** ZDI-CAN-19902
- **Date:** 2023-04-24
- **CVE:** CVE-2022-47505
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Performance Monitor
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-458/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds Network Performance Monitor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of the TFTP Server service. By creating a junction, an attacker can abuse the service to create or read arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://www.solarwinds.com/trust-center/security-advisories/cve-2022-47505

## Disclosure Timeline

- 2022-12-22 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
