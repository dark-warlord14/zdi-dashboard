# ZDI-17-520: (0Day) Eaton ELCSoft ELCSimulator Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-520
- **ZDI-CAN:** ZDI-CAN-4037
- **Date:** 2017-08-07
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Eaton
- **Affected Products:** ELCSoft
- **Credit:** Ariele Caltabiano(kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-520/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Eaton ELCSoft. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of network TCP requests by ELCSimulator.exe. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/11/2016 - ZDI disclosed the report to ICS-CERT 11/01/2016 - The vendor requested additional details from ZDI through ICS-CERT 11/07/2016 - ZDI provided additional details as requested 03/13/2017, 03/17/2017, and 03/29/2017 - ICS-CERT replied that the vendor cannot validate these on the latest and asked if ZDI could re-vet against their latest version 04/05/2017 - ZDI replied that this report still hits 07/12/2017 - ZDI requested an update from ICS-CERT 07/13/2017 - ICS-CERT indicated that to their knowledge the vendor has not yet created a relevant patch 07/20/2017 - ZDI notified the vendor of the intention to publish the report as 0-day -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2016-10-11 - Vulnerability reported to vendor
- 2017-08-07 - Coordinated public release of advisory
