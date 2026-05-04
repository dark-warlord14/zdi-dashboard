# ZDI-19-862: Jenkins dingding-notifications Cleartext Storage of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-862
- **ZDI-CAN:** ZDI-CAN-8833
- **Date:** 2019-10-04
- **CVE:** CVE-2019-10433
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Jenkins
- **Affected Products:** dingding-notifications
- **Credit:** David Fiser (Trend Micro Team Nebula)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-862/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Jenkins. Authentication is required to exploit this vulnerability. The specific flaw exists within the dingding-notifications plugin. The issue results from storing credentials in plaintext. An attacker can leverage this vulnerability to execute code in the context of the build process.

## Additional Details

Jenkins has issued an update to correct this vulnerability. More details can be found at: https://jenkins.io/security/advisory/2019-10-01/

## Disclosure Timeline

- 2019-06-11 - Vulnerability reported to vendor
- 2019-10-04 - Coordinated public release of advisory
