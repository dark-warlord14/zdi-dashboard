# ZDI-20-634: Advantech WebAccess/SCADA BwBacNetJ Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-634
- **ZDI-CAN:** ZDI-CAN-10080
- **Date:** 2020-05-08
- **CVE:** CVE-2020-12002
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/SCADA
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-634/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/SCADA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the BwBacNetJ driver. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-128-36

## Disclosure Timeline

- 2020-03-25 - Vulnerability reported to vendor
- 2020-05-08 - Coordinated public release of advisory
