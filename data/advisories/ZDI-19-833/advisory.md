# ZDI-19-833: Jenkins Skytap Cloud CI Cleartext Storage of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-833
- **ZDI-CAN:** ZDI-CAN-8875
- **Date:** 2019-09-17
- **CVE:** CVE-2019-10366
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Jenkins
- **Affected Products:** Skytap
- **Credit:** David Fiser (Trend Micro Team Nebula)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-833/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Jenkins Skytap Cloud CI. Authentication is required to exploit this vulnerability. The specific flaw exists within the Skytap Cloud CI plugin. The issue results from storing credentials in plaintext. An attacker can leverage this vulnerability to execute code in the context of the build process.

## Additional Details

Jenkins has issued an update to correct this vulnerability. More details can be found at: https://jenkins.io/security/advisory/2019-07-31/

## Disclosure Timeline

- 2019-06-18 - Vulnerability reported to vendor
- 2019-09-17 - Coordinated public release of advisory
