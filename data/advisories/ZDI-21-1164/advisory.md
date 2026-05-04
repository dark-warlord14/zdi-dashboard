# ZDI-21-1164: Fatek Automation Communication Server Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1164
- **ZDI-CAN:** ZDI-CAN-13791
- **Date:** 2021-10-14
- **CVE:** CVE-2021-38432
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fatek Automation
- **Affected Products:** Communication Server
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fatek Automation Communication Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of data sent to the Facon Server, which listens on port 500 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the FaconSvr process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-280-07

## Disclosure Timeline

- 2021-06-11 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
