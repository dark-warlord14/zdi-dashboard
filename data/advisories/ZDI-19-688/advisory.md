# ZDI-19-688: LAquis SCADA LQS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-688
- **ZDI-CAN:** ZDI-CAN-8198
- **Date:** 2019-08-05
- **CVE:** CVE-2019-10994
- **CVSS:** 2.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-688/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LQS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-213-06

## Disclosure Timeline

- 2019-04-03 - Vulnerability reported to vendor
- 2019-08-05 - Coordinated public release of advisory
