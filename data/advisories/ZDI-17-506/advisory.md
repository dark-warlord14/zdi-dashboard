# ZDI-17-506: Mitsubishi Electric E-Designer TxStaticString Col Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-506
- **ZDI-CAN:** ZDI-CAN-3759
- **Date:** 2017-08-01
- **CVE:** CVE-2017-9634
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mitsubishi Electric
- **Affected Products:** E-Designer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-506/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mitsubishi Electric E-Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of TxStaticString sections of a mpa (project specification) file. An out-of-bounds value for the column specification will cause a user-supplied string to be written to an arbitrary memory address. An attacker can leverage this vulnerability to execute arbitrary code in the context of the Administrator.

## Additional Details

Mitsubishi Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-213-01

## Disclosure Timeline

- 2016-05-31 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
