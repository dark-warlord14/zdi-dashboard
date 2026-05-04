# ZDI-19-689: LAquis SCADA LQS File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-689
- **ZDI-CAN:** ZDI-CAN-8200
- **Date:** 2019-08-05
- **CVE:** CVE-2019-10980
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-689/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LQS files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-213-06

## Disclosure Timeline

- 2019-04-03 - Vulnerability reported to vendor
- 2019-08-05 - Coordinated public release of advisory
