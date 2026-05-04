# ZDI-21-208: Avast Premium Security AvastSvc Directory Junction Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-208
- **ZDI-CAN:** ZDI-CAN-12082
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27241
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Avast
- **Affected Products:** Premium Security
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-208/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary directories on affected installations of Avast Premium Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AvastSvc.exe module. By creating a directory junction, an attacker can abuse the service to delete a directory. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in Avast v20.10

## Disclosure Timeline

- 2020-11-18 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
