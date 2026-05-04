# ZDI-25-654: SolarWinds TFTP Server Deserialization of Untrusted Data Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-654
- **ZDI-CAN:** ZDI-CAN-26280
- **Date:** 2025-07-28
- **CVE:** CVE-2025-26397
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** TFTP Server
- **Credit:** ccc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-654/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds TFTP Server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the internal TFTP communications endpoint, which listens on the localhost interface on TCP port 8099 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/hco_2025-2-1_release_notes.htm

## Disclosure Timeline

- 2025-05-02 - Vulnerability reported to vendor
- 2025-07-28 - Coordinated public release of advisory
- 2025-07-28 - Advisory Updated
