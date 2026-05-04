# ZDI-22-1450: Advantech R-SeeNet out Endpoint Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1450
- **ZDI-CAN:** ZDI-CAN-17392
- **Date:** 2022-10-21
- **CVE:** CVE-2022-3386
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** R-SeeNet
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1450/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech R-SeeNet. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of POST requests sent to the out.php endpoint. When processing the filename and path elements, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-291-01

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
