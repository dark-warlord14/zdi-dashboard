# ZDI-19-932: Jenkins NeoLoad Cleartext Storage of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-932
- **ZDI-CAN:** ZDI-CAN-8873
- **Date:** 2019-10-30
- **CVE:** CVE-2019-10440
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Jenkins
- **Affected Products:** NeoLoad
- **Credit:** David Fiser (Trend Micro Team Nebula)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-932/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Jenkins NeoLoad. Authentication is required to exploit this vulnerability. The specific flaw exists within the NeoLoad plugin. The issue results from storing credentials in plaintext. An attacker can leverage this vulnerability to execute code in the context of the build process.

## Additional Details

Jenkins has issued an update to correct this vulnerability. More details can be found at: https://jenkins.io/security/advisory/2019-10-16/

## Disclosure Timeline

- 2019-06-18 - Vulnerability reported to vendor
- 2019-10-30 - Coordinated public release of advisory
