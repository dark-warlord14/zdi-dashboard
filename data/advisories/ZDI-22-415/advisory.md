# ZDI-22-415: (Pwn2Own) Cisco RV340 NGINX Improper Authentication Unrestricted File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-415
- **ZDI-CAN:** ZDI-CAN-15848
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20705
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Q. Kaiser from IoT Inspector Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-415/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Cisco RV340 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the NGINX web server. When parsing the Authorization request header, the server does not properly validate user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to create files in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
