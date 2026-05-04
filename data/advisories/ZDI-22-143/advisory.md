# ZDI-22-143: Bitdefender GravityZone Link Following Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-143
- **ZDI-CAN:** ZDI-CAN-13801
- **Date:** 2022-01-27
- **CVE:** CVE-2021-3641
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Bitdefender
- **Affected Products:** GravityZone
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-143/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Bitdefender GravityZone. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Endpoint Agent. By creating a symbolic link, an attacker can abuse the service to overwrite a file. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Bitdefender has issued an update to correct this vulnerability. More details can be found at: https://www.bitdefender.com/support/security-advisories/improper-link-resolution-before-file-access-in-bitdefender-endpoint-security-tools-for-windows-va-9921/

## Disclosure Timeline

- 2021-07-09 - Vulnerability reported to vendor
- 2022-01-27 - Coordinated public release of advisory
